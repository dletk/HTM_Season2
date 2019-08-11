from django.urls import path
from .forms import TangTocQuestionForm
from .views import NewQuestion

urlpatterns = [
    path("newQuestion/", NewQuestion.as_view(), name="newTangTocQuestion"),
]
