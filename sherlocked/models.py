from django.db import models
from django.contrib.auth.models import User

class userDetails(models.Model):
	zealid = models.CharField(max_length = 70)
	question = models.IntegerField(default = 0)
	lastsolvedAt = models.DateTimeField(auto_now_add=True)


class Questions(models.Model):
	description = models.CharField(max_length = 10000)
	answer = models.CharField(max_length = 1000)
	hint = models.CharField(max_length = 1000)
	waittime = models.CharField(max_length = 100)
