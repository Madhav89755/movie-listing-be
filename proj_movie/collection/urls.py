from django.urls import path
from .views import CreateCollectionView

urlpatterns=[
    path("collection/", CreateCollectionView.as_view())
]