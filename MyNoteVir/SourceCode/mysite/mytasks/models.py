from django.db import models

# Create your models here.
class User(models.Model):
	user_number = models.IntegerField()
	first_name = models.CharField(max_length=200)
	last_name = models.CharField(max_length=200)
	user_name = models.CharField(max_length=50)
	email = models.CharField(max_length=100)
	password = models.CharField(max_length=200)
	def __str__(self):
		return self.user_name

class Task(models.Model):
	task_number = models.IntegerField()
	title = models.CharField(max_length=500)
	description = models.CharField(max_length=3000)
	owner = models.ForeignKey(User, on_delete=models.CASCADE)
	def __str__(self):
		return self.title
