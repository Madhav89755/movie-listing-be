from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from utils.logging import unknown_exception_logger
from .models import Collection
from .serializers import CreateCollectionSerializer, CollectionSerializer
from .fetch import fetch_collection_data, fetch_collection_details
from movies.serializers import CreateMovieSerializer
# Create your views here.


class CollectionView(APIView):
    def post(self, request, *args, **kwargs):
        request.data['user'] = self.request.user.id
        status_code = status.HTTP_201_CREATED
        try:
            resp = CreateCollectionSerializer(data=request.data)
            resp.is_valid(raise_exception=True)
            resp.save()
            resp = resp.data
        except Exception as e:
            resp = {"error": str(e)}
            status_code = status.HTTP_400_BAD_REQUEST
        return Response(resp, status=status_code)

    def get(self, request, *args, **kwargs):
        status_code = status.HTTP_201_CREATED
        resp = {
            "is_success": True
        }
        try:
            resp['data'] = fetch_collection_data(
                user_id=int(self.request.user.id))
        except Exception as e:
            resp['is_success'] = False
            resp = {"error": unknown_exception_logger(e)}
            status_code = status.HTTP_400_BAD_REQUEST
        return Response(resp, status=status_code)


class CollectionManagementView(APIView):
    def get(self, request, collection_uuid):
        context = {}
        status_code = status.HTTP_200_OK
        try:
            context['data'] = fetch_collection_details(user_id=self.request.user.id,
                                                       collection_id=collection_uuid)
        except Exception as e:
            context['error'] = unknown_exception_logger(e)
            status_code = status.HTTP_400_BAD_REQUEST
        return Response(context, status_code)

    def delete(self, request, collection_uuid):
        try:
            Collection.objects.get(id=collection_uuid).delete()
            context = {"message": "Deletion Success"}
            status_code = status.HTTP_200_OK
        except Exception as e:
            context = {"error": unknown_exception_logger(e)}
            status_code = status.HTTP_400_BAD_REQUEST
        return Response(context, status_code)

    def put(self, request, collection_uuid):
        try:
            data = request.data
            movie_data = request.data.pop("movies", None)

            collection_obj = Collection.objects.get(id=collection_uuid)

            serializer_obj = CollectionSerializer(
                instance=collection_obj, data=data, partial=True)
            serializer_obj.is_valid(raise_exception=True)
            serializer_obj.save()

            eligible_movies=[]
            if movie_data:
                for movie in movie_data:
                    movie['collection']=collection_uuid

                movie_data=CreateMovieSerializer(data=movie_data, many=True)
                movie_data.is_valid(raise_exception=True)
                movie_data.save()

            context = {"message": "Updation Success"}
            status_code = status.HTTP_200_OK
        except Exception as e:
            context = {"error": unknown_exception_logger(e)}
            status_code = status.HTTP_400_BAD_REQUEST
        return Response(context, status_code)
