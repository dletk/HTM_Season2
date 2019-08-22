from django.shortcuts import render
from django.http.response import HttpResponse, JsonResponse, HttpResponseForbidden
from django.contrib.auth.decorators import login_required
from django.views import generic
from django.urls import reverse_lazy

from .models import DiemThiSinh

from khoidong.models import KhoiDongQuestion
from vuotsong.models import VuotSongQuestion
from tangtoc.models import TangTocQuestion

from khoidong.forms import KhoiDongAnswerForm
from vuotsong.forms import VuotSongAnswerForm

import json

currentQuestionContent = ""
currentQuestionID = 0
currentRound = "khoidong"

# TODO: Add form classes for other rounds here
FORM_CLASSES = {
                "khoidong": KhoiDongAnswerForm,
                "vuotsong": VuotSongAnswerForm,
                }

currentRinger = ""

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
                diemThiSinhManager.updateScore(username, score)
                return HttpResponse("Success!")
            else:
                # This user is not allowed to do the update
                return HttpResponse("Not allowed to access")


class NewAnswer(generic.CreateView):
    """
    Class-based view to submit a new answer to the database
    """
    global currentQuestionID, currentRound, FORM_CLASSES

    form_class = FORM_CLASSES[currentRound]
    success_url = reverse_lazy("answer")
    template_name = "baseForm.html"

    # Handle the post method to inlcude question number and
    def post(self, request):
        # If currently no question is being presented, prevent thi sinh to submit answer
        if currentQuestionID > 0:
            print("==========> Current round: {}".format(currentRound))
            self.form_class = FORM_CLASSES[currentRound]

            user = request.user
            # Get the form data submitted by user
            formAnswer = self.form_class(request.POST)
            # Create an answer instance but not yet saved
            answer = formAnswer.save(commit=False)
            answer.thisinh = user

            print("===== Current form {}, curent round {}".format(self.form_class, currentRound))

            # Find the correct round
            # Only these 2 rounds require submission to server
            if currentRound == "khoidong":
                answer.question = KhoiDongQuestion.objects.get(questionID=currentQuestionID)
            elif currentRound == "vuotsong":
                answer.question = VuotSongQuestion.objects.get(questionID=currentQuestionID)
            
        
            # Save the answer
            answer.save()

        # Return a new page for the next question
        form = self.form_class()
        return render(request, template_name=self.template_name, context={"form": form, "answerView": True})

    def get(self, request):
        form = self.form_class()
        return render(request, template_name=self.template_name, context={"form": form, "answerView": True})


def currentQuestion(request):
    """
    Function to handle the request for retrieve or updating current question

    Accepted methods:
        GET: Return the current question content in JSON format
        POST: Update the current question content
    """ 
    global currentQuestionContent, currentQuestionID, currentRound

    if request.method == "GET":
        return JsonResponse(json.dumps(dict(question=currentQuestionContent)), safe=False)
    elif request.method == "POST":
        if request.user.is_staff:
            dataPost = request.POST
            
            # Update the data for server to know about current question info
            currentQuestionContent = dataPost.get("question")
            currentQuestionID = int(dataPost.get("questionID"))
            currentRound = dataPost.get("round")
            return HttpResponse("Updated!")
        else:
            return HttpResponseForbidden()

def ringBell(request):
    """
    Function to handle the request for retrieve or updating current ringer

    Accepted methods:
        GET: Return the current ringer name in JSON format
        POST: Update the current ringer name
    """ 
    global currentRinger

    if request.method == "GET":
        # Return currentRinger
        result = {"ringerName": currentRinger}
        return JsonResponse(json.dumps(result), safe=False)
    elif request.method == "POST":
        # Another person ringed
        if len(currentRinger) > 0:
            return HttpResponseForbidden()
        currentRinger = str(request.user)
        print(currentRinger, "ringed a bell!")
        return HttpResponse("Ringed!")

def resetRingingState(request):
    """
    Function to reset the state of the bell
    """ 
    global currentRinger

    # Only POST method is allowed
    if request.method != "POST":
        return HttpResponseForbidden()

    if request.user.is_staff:
        # Reset by assigning currentRinger to be an empty string
        currentRinger = ""
        return HttpResponse("Already reset!")
    else:
        return HttpResponseForbidden()