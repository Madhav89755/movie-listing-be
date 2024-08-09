from django.urls import path
from .views import GetMoviesAPI

urlpatterns=[
    path("movies", GetMoviesAPI.as_view())
]