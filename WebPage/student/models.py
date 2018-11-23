from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

class StudentProfile(models.Model):
	name = models.CharField(max_length=20)
	age = models.IntegerField()
	gender = models.CharField(max_length=10)
