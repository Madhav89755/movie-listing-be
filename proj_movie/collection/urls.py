from django.urls import path
from .views import CollectionView, CollectionManagementView

urlpatterns=[
    path("collection/", CollectionView.as_view()),
    path("collection/<str:collection_uuid>", CollectionManagementView.as_view())
]