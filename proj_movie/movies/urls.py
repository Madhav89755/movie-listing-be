from django.urls import path
from .views import GetMoviesAPI, UserRegisterView

urlpatterns=[
    path("movies", GetMoviesAPI.as_view()),
    path("register", UserRegisterView.as_view())
]