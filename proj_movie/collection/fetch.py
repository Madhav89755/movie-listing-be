import uuid
from .models import Collection
from .serializers import CollectionSerializer
from movies.models import Genres

def fetch_collection_data(user_id:int, include_movies:bool=False)->dict:
    """ Fetch data for collections """

    collection_data={}
    collection_data['collections']=[]
    collection_data['favourite_genres']=""

    obj=Collection.objects.filter(user_id=user_id)
    if obj.count()>0:
        data_serialized=CollectionSerializer(instance=obj, many=True).data
        genre_obj=Genres.objects.filter(user_id=user_id)
        genre_data=genre_obj[:3].values_list("genre", flat=True)

        print(data_serialized)
        if not include_movies:
            [elements.pop("movies") for elements in data_serialized]

        collection_data['collections']=data_serialized
        collection_data['favourite_genres']=", ".join(genre_data)

    return collection_data

def fetch_collection_details(user_id:int, collection_id:uuid)->dict:
    """ Fetch data for collections """

    obj=Collection.objects.get(user_id=user_id, id=collection_id)
    data_serialized=CollectionSerializer(instance=obj).data

    collection_data={}
    collection_data['collections']=data_serialized,

    return collection_data
