from rest_framework import serializers
from django.contrib.auth.models import User
from collection.models import Collection
from movies.serializers import CreateMovieSerializer

class CreateCollectionSerializer(serializers.ModelSerializer):
    title=serializers.CharField(source="collection_title", write_only=True)
    description=serializers.CharField(max_length=None, write_only=True)
    collection_uuid=serializers.UUIDField(source="id", read_only=True)
    movies=serializers.ListField(write_only=True)
    class Meta:
        model=Collection
        fields=["collection_uuid",
                "title",
                "user",
                "description",
                "movies"]
        extra_kwargs = {'user': {'write_only': True}}

    def create(self, validated_data):
        movies_data=validated_data.pop('movies', [])
        data=super().create(validated_data)
        for movie in movies_data:
            movie['collection']=data.id
        movie_data=CreateMovieSerializer(data=movies_data, many=True)
        movie_data.is_valid(raise_exception=True)
        movie_data.save()
        return data