from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.views import generic
from django.urls import reverse_lazy

from .forms import KhoiDongQuestionForm


# Create your views here.
class NewQuestion(generic.CreateView):
    """
    Class-based view to handle creating a new question
    Usig a class-based view will provides us a defautl error-handling
    """

    form_class = KhoiDongQuestionForm
    success_url = reverse_lazy("newKhoiDongQuestion")
    template_name = "baseForm.html"

    def get(self, request, *args, **kwargs):
        if request.user.is_staff:
            form = self.form_class()
            return render(request, template_name="baseForm.html", 
                                    context={"form": form})
        else:
            return render(request, template_name="home.html",
                                    context={"message": "Xin lỗi, bạn không được phép truy cập tính năng này"})
