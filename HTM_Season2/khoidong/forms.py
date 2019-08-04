from django.forms import ModelForm
from .models import KhoiDongQuestion

class KhoiDongQuestionForm(ModelForm):
    """
    The form to create a new Khoi Dong question
    """

    class Meta:
        model = KhoiDongQuestion
        fields = "__all__"