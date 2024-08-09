from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from utils.logging import unknown_exception_logger
from .serializers import CreateCollectionSerializer
from .fetch import fetch_collection_data
# Create your views here.

class CreateCollectionView(APIView):
    def post(self, request, *args, **kwargs):
        request.data['user']=self.request.user.id
        status_code=status.HTTP_201_CREATED
        try:
            resp=CreateCollectionSerializer(data=request.data)
            resp.is_valid(raise_exception=True)
            resp.save()
            resp=resp.data
        except Exception as e:
            resp={"error": str(e)}
            status_code=status.HTTP_400_BAD_REQUEST
        return Response(resp, status=status_code)

    def get(self, request, *args, **kwargs):
        status_code=status.HTTP_201_CREATED
        resp={
            "is_success":True
        }
        try:
            resp['data']=fetch_collection_data(user_id=self.request.user.id)
        except Exception as e:
            resp['is_success']=False
            resp={"error": unknown_exception_logger(e)}
            status_code=status.HTTP_400_BAD_REQUEST
        return Response(resp, status=status_code)

