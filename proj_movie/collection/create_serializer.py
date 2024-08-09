from rest_framework import serializers
from collection.models import Collection

class CreateCollectionSerializer(serializers.ModelSerializer):
    title=serializers.CharField(source="collection_title")
    class Meta:
        model=Collection
        fields=["title",
                "user",
                "description",]
