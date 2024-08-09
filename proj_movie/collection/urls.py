from django.urls import path
from .views import CollectionView, CollectionManagementView

urlpatterns=[
    path("", CollectionView.as_view()),
    path("<str:collection_uuid>", CollectionManagementView.as_view())
]