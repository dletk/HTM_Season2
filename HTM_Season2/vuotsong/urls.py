from django.urls import path
from .views import getQuestions

urlpatterns = [
    path("", getQuestions, name="vuotsong")
]