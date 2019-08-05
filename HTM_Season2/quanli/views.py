from django.shortcuts import render
from django.http.response import HttpResponse, JsonResponse, HttpResponseForbidden
from django.contrib.auth.decorators import login_required

from .models import DiemThiSinh

import json

currentQuestionContent = ""

# Create your views here.
@login_required
def score(request, username=None, score=None):
    """
    Function to handle the request to grading page

    Accepted methods:
        GET: Get the information of current grading, available to all users
        If username and score is provided, attempt to change the info in database
    Params:
        username: username of the contestant to be updated
        score: new score
    """

    diemThiSinhManager = DiemThiSinh.objects

    if request.method == "GET":
        if username is None:
            # This request is for grading info
            scores = diemThiSinhManager.getAllScore()
            return render(request, template_name="quanli/score.html", context={"scores": scores})
        else:
            # This request is for updating
            if request.user.is_staff:
                # TODO: Update the information in database and return OK
                diemThiSinhManager.updateScore(username, score)
                return HttpResponse("Success!")
            else:
                # This user is not allowed to do the update
                return HttpResponse("Not allowed to access")


def currentQuestion(request):
    """
    Function to handle the request for retrieve or updating current question

    Accepted methods:
        GET: Return the current question content in JSON format
        POST: Update the current question content
    """ 
    global currentQuestionContent

    if request.method == "GET":
        return JsonResponse(json.dumps(dict(question=currentQuestionContent)), safe=False)
    elif request.method == "POST":
        if request.user.is_staff:
            currentQuestionContent = request.POST.get("question")
            return HttpResponse("Updated!")
        else:
            return HttpResponseForbidden()
