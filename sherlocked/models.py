from django.db import models
from django.contrib.auth.models import User

class UserDetail(models.Model):
    Zealid = models.CharField(max_length = 70)
    CurrentQuestionNo = models.IntegerField(default = 0)
    LastSolvedAt = models.CharField(max_length = 10000)
    college = models.CharField(max_length = 10000)
    phno = models.CharField(max_length = 100)

class Question(models.Model):
    Question = models.TextField(max_length = 10000)
    Answer = models.CharField(max_length = 1000)
    WaitTime = models.CharField(max_length = 100)
    WaitMessage = models.TextField(max_length = 100000)
    question_story = models.TextField(max_length = 10000)
