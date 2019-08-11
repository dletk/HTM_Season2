from django.db import models
from userprofile.models import MyUser

# Create your models here.
class TangTocQuestion(models.Model):
    """
    Model for questions in Tang Toc round
    """
    # No need to create a question ID in this case, Django will generate a primary key for each question

    # The text content of the question
    questionText = models.TextField(blank=False, verbose_name="Nội dung câu hỏi")

    FIELDS = [("Toan", "Toán"), ("Ly", "Lý"), ("Hoa", "Hoá")]
    # The field of this question
    questionField = models.CharField(max_length=50, verbose_name="Lĩnh vực",
                                     choices = FIELDS)

    # The answer for this question
    answer = models.CharField(max_length=255, blank=False, verbose_name="Đáp án")

    def __str__(self):
        return self.questionField + ": " + self.questionText


# This round does not need to have Answer model because the contestant will answer directly to MC
