from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView
from .views import GetMoviesAPI, UserRegisterView

from drf_yasg.utils import swagger_auto_schema

decorated_login_view = \
    swagger_auto_schema(
        operation_description="Obtain the Access Token and Refresh Token for the registered user",
        operation_id="Login",
        tags=['Accounts'],
        security=[],
        method='post'
    )(TokenObtainPairView.as_view())


urlpatterns = [
    path("movies", GetMoviesAPI.as_view()),
    path("register", UserRegisterView.as_view()),
    path("login", decorated_login_view)
]
