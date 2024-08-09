from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST
# Create your views here.
from .fetch import fetch_movies


class GetMoviesAPI(APIView):
    def get(self, request):
        status=HTTP_400_BAD_REQUEST
        page=request.query_params.get("page")
        response=fetch_movies(page)
        if isinstance(response, tuple):
            status, data=response
        else:
            data={"response":response}
        return Response(data, status)
