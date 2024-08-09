from django.shortcuts import render
from rest_framework import generics
# Create your views here.
from .create_serializer import CreateCollectionSerializer
from .models import Collection

class CreateCollectionView(generics.CreateAPIView):
    queryset=Collection.objects.all()
    serializer_classes=CreateCollectionSerializer