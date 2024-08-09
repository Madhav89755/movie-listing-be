from .models import Collection
from .serializers import CollectionSerializer
from movies.models import Genres

def fetch_collection_data(user_id:int)->dict:
    """ Fetch data for collections """

    obj=Collection.objects.filter(user_id=user_id)
    data_serialized=CollectionSerializer(instance=obj, many=True)
    genre_obj=Genres.objects.filter(user_id=user_id)
    genre_data=genre_obj[:3].values_list("genre", flat=True)

    collection_data={}
    collection_data['collections']=data_serialized.data,
    collection_data['favourite_genres']=", ".join(genre_data)

    return collection_data
