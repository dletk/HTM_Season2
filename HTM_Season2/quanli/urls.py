from django.urls import path
from .views import score, currentQuestion, NewAnswer, ringBell, resetRingingState

urlpatterns = [
    # Handle grading requests
    path("score/", score, name="score"),
    path("score/<str:username>/<int:score>", score, name="updateScore"),
    path("currentQuestion/", currentQuestion, name="currentQuestion"),
    # Handle submiting answer
    path("answer/", NewAnswer.as_view(), name="answer"),
    # Handle ringing request
    path("ringBell/", ringBell, name="ringBell"),
    path("resetRingingState/", resetRingingState, name="resetRingingState")
]
