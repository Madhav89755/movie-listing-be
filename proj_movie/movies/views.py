from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.status import HTTP_400_BAD_REQUEST
from django.contrib.auth.models import User

from .serializers import UserRegistrationSerializer
from .fetch import fetch_movies

# Create your views here.


class UserRegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = UserRegistrationSerializer

    def post(self, request, *args, **kwargs):
        try:
            return super().post(request, *args, **kwargs)
        except Exception as e:
            return Response({"error": str(e)}, status=HTTP_400_BAD_REQUEST)


class GetMoviesAPI(APIView):
    def get(self, request):
        status = HTTP_400_BAD_REQUEST
        page = request.query_params.get("page")
        response = fetch_movies(page)
        if isinstance(response, tuple):
            status, data = response
        else:
            data = {"response": response}
        return Response(data, status)
