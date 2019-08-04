from django.urls import path
from .views import NewQuestion

urlpatterns = [
    path("newQuestion/", NewQuestion.as_view(), name="newKhoiDongQuestion")
]