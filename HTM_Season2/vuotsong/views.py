from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def getQuestions(request):
    """
    Function to view all questions for Vuot Song round. Format: JSON
    """
    html = "Vuot Song: " + str(request) 
    return HttpResponse(html)