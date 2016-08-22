from django.db import models

# Create your models here.

class Reminder(models.Model):
	title = models.CharField(max_length=50)
	description = models.CharField(max_length=150)

	deadline = models.DateTimeField()

	# Location of event in longitude and lattitude
	lon = models.FloatField()
	lat = models.FloatField()

	priority = models.IntegerField()

class Task(Reminder):
	# Estimated time to completion in seconds (a time interval object)
	etc = models.DurationField()

class Event(Reminder):
	start = models.DateTimeField()
	end = models.DateTimeField()