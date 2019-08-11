from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy

from .forms import TangTocQuestionForm

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
