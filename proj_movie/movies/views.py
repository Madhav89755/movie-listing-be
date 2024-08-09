from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.status import HTTP_400_BAD_REQUEST
from django.contrib.auth.models import User

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

from .serializers import UserRegistrationSerializer
from .fetch import fetch_movies


# Create your views here.


class UserRegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = UserRegistrationSerializer

    @swagger_auto_schema(
        operation_description="Register a user onto the platform to perform operations.",
        operation_id="Register User",
        tags=["Accounts"]
    )
    def post(self, request, *args, **kwargs):
        try:
            return super().post(request, *args, **kwargs)
        except Exception as e:
            return Response({"error": str(e)}, status=HTTP_400_BAD_REQUEST)


class GetMoviesAPI(APIView):
    @swagger_auto_schema(
        operation_description="Fetch Movie List from the third party api.",
        operation_id="Fetch Movies",
        tags=["Movies"],
        manual_parameters=[
            openapi.Parameter(
                name="page",
                in_=openapi.IN_QUERY,
                type=openapi.TYPE_INTEGER,
                description="Page number for next set of movies"
            )
        ]
    )
    def get(self, request):
        status = HTTP_400_BAD_REQUEST
        page = request.query_params.get("page")
        response = fetch_movies(page)
        if isinstance(response, tuple):
            status, data = response
        else:
            data = {"response": response}
        return Response(data, status)
