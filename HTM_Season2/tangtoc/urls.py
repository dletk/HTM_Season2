from django.urls import path
from .forms import TangTocQuestionForm
from .views import NewQuestion, getAvailableFields

urlpatterns = [
    path("newQuestion/", NewQuestion.as_view(), name="newTangTocQuestion"),
    path("getField/", getAvailableFields, name="tangtoc"),
]
