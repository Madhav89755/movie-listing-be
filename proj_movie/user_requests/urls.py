from django.urls import path
from .views import RequestCountAPI, RequestCountResetAPI

urlpatterns = [
    path("", RequestCountAPI.as_view()),
    path("reset/", RequestCountResetAPI.as_view())
]
