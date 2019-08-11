from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy

from .forms import TangTocQuestionForm
from .models import TangTocQuestion, TangTocQuestionField

# Create your views here.


class NewQuestion(CreateView):
    """
    Class-based view to handle creating a new question
    Usig a class-based view will provides us a defautl error-handling
    """

    form_class = TangTocQuestionForm
    success_url = reverse_lazy("newTangTocQuestion")
    template_name = "baseForm.html"

    def get(self, request, *args, **kwargs):
        if request.user.is_staff:
            form = self.form_class()
            return render(request, template_name="baseForm.html",
                          context={"form": form})
        else:
            return render(request, template_name="home.html",
                          context={"message": "Xin lỗi, bạn không được phép truy cập tính năng này"})


def getAvailableFields(request):
    """
    View to handle the request for get the current remaining available fields
    """
    availableFields = []

    for field in TangTocQuestionField.objects.all():
        if not field.used:
            availableFields.append(field)

    print(availableFields)
    return render(request, template_name="tangtoc/tangtocField.html", context={"fields": availableFields,
                                                               "numFields": range(len(availableFields))})


def getNewQuestion(request, field):
    """
    Function to handle request to get a new set of questions

    Params:
        fields (string): The field of the set of questions
    Return:
        questions (QuerySet): The set of questiosn for this contestant
    """
