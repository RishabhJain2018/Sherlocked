from django.db import models
from django.contrib.auth.models import User

class UserDetail(models.Model):
	Zealid = models.CharField(max_length = 70)
	CurrentQuestionNo = models.IntegerField(default = 0)
	LastSolvedAt = models.CharField(max_length = 10000)

class Question(models.Model):
	QuestionTitle = models.CharField(max_length = 1000)
	Description = models.CharField(max_length = 10000)
	Answer = models.CharField(max_length = 1000)
	Hint = models.CharField(max_length = 1000)
	WaitTime = models.CharField(max_length = 100)
	WaitMessage = models.CharField(max_length = 100000)


