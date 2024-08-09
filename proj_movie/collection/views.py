from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
# Create your views here.
from .create_serializer import CreateCollectionSerializer
from .models import Collection

class CreateCollectionView(generics.CreateAPIView):
    queryset=Collection.objects.all()
    serializer_class=CreateCollectionSerializer
    
    def post(self, request, *args, **kwargs):
        request.data['user']=self.request.user.id
        status_code=status.HTTP_201_CREATED
        try:
            resp=super().post(request, *args, **kwargs).data
        except Exception as e:
            resp={"error": str(e)}
            status_code=status.HTTP_400_BAD_REQUEST
        return Response(resp, status=status_code)

