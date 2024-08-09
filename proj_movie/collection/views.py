import pandas as pd
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from drf_yasg.utils import swagger_auto_schema

from utils.logging import unknown_exception_logger
from utils.static_messages import UPDATE_SUCCESS, DELETE_SUCCESS
from collection.models import Collection
from collection.serializers import (
    CreateCollectionSerializer, CollectionSerializer)
from collection.fetch import (fetch_collection_data, fetch_collection_details)
from collection.swagger_configs.collection import (
    COLLECTION_CREATION_UPDATED_SCHEMA, PATH_COLLECTION_ID)

from movies.serializers import CreateMovieSerializer
# Create your views here.


class CollectionView(APIView):
    @swagger_auto_schema(
        operation_description="Create a Collection for movies",
        operation_id="Create Collection",
        tags=['Collection'],
        request_body=COLLECTION_CREATION_UPDATED_SCHEMA
    )
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

    @swagger_auto_schema(
        operation_description="Get list of all existing Collection \
            for logged in user",
        operation_id="Get Collection list",
        tags=['Collection'],
        manual_parameters=[PATH_COLLECTION_ID],
    )
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
    @swagger_auto_schema(
        operation_description="Get details of an existing Collection",
        operation_id="Get Collection Details",
        tags=['Collection'],
        manual_parameters=[PATH_COLLECTION_ID],
    )
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

    @swagger_auto_schema(
        operation_description="Delete an existing Collection of movies",
        operation_id="Delete Collection",
        tags=['Collection'],
        manual_parameters=[PATH_COLLECTION_ID],
    )
    def delete(self, request, collection_uuid):
        try:
            Collection.objects.get(id=collection_uuid).delete()
            context = {"message": DELETE_SUCCESS}
            status_code = status.HTTP_200_OK
        except Exception as e:
            context = {"error": unknown_exception_logger(e)}
            status_code = status.HTTP_400_BAD_REQUEST
        return Response(context, status_code)

    @swagger_auto_schema(
        operation_description="Update an existing Collection for movies, \
            each parameter in the body is optional",
        operation_id="Update Collection",
        tags=['Collection'],
        manual_parameters=[PATH_COLLECTION_ID],
        request_body=COLLECTION_CREATION_UPDATED_SCHEMA
    )
    def put(self, request, collection_uuid):
        try:
            data = request.data
            movie_data = request.data.pop("movies", None)

            collection_obj = Collection.objects.get(id=collection_uuid)

            serializer_obj = CollectionSerializer(
                instance=collection_obj, data=data, partial=True)
            serializer_obj.is_valid(raise_exception=True)
            collection_obj = serializer_obj.save()

            if movie_data:
                df = pd.DataFrame(movie_data)
                df['collection'] = collection_uuid
                movie_data = df.to_dict(orient="records")

                movie_data = CreateMovieSerializer(data=movie_data, many=True)
                movie_data.is_valid(raise_exception=True)
                movie_data.save()

            context = {"message": UPDATE_SUCCESS}
            status_code = status.HTTP_200_OK
        except Exception as e:
            context = {"error": unknown_exception_logger(e)}
            status_code = status.HTTP_400_BAD_REQUEST
        return Response(context, status_code)
