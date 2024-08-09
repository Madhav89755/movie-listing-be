from django.urls import path
from .views import GetMoviesAPI, UserRegisterView
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns=[
    path("movies", GetMoviesAPI.as_view()),
    path("register", UserRegisterView.as_view()), 
    path("login", TokenObtainPairView.as_view()), 
]