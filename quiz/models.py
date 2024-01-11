from django.db import models

# Create your models here.
# models.py
from django.db import models

class Category(models.Model):
    category_name = models.CharField(max_length=100)
    def __str__(self) -> str:
        return self.category_name


class Question(models.Model):
    category = models.ForeignKey(Category, related_name='questions', on_delete=models.CASCADE)
    question_text = models.CharField(max_length=255)
    def __str__(self) -> str:
        return self.question_text


class Answer(models.Model):
    question = models.ForeignKey(Question, related_name='answers', on_delete=models.CASCADE)
    answer_text = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)
    def __str__(self) -> str:
        return self.answer_text

