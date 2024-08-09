from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView
from .views import GetMoviesAPI, UserRegisterView

urlpatterns = [
    path("movies", GetMoviesAPI.as_view()),
    path("register", UserRegisterView.as_view()),
    path("login", TokenObtainPairView.as_view())
]
