from django.db import models

# Create your models here.

# Actions with a due date.
class Reminder(models.Model):
	title = models.CharField(max_length=50)
	description = models.CharField(max_length=150, blank=True) # Not required

	deadline = models.DateTimeField()

	# Location of event in longitude and lattitude
	lon = models.FloatField(blank=True) # Not required
	lat = models.FloatField(blank=True) # Not required

	priority = models.IntegerField()

	def __str__(self):
		return self.title

# Tasks are longer and should have an ETC. 
class Task(Reminder):
	# Estimated time to completion in seconds (a time interval object)
	etc = models.DurationField()

# Events are scheduled on a calendar and can be rescheduled.
class Event(Reminder):
	start = models.DateTimeField()
	end = models.DateTimeField()

	calendar = models.ForeignKey('Calendar', on_delete=models.CASCADE)

# Calendars hold lists of event objects. Reminders and tasks are scheduled onto calendars. EVENTS CAN BE RESCHEDULED HENCE THE DUE DATE.
class Calendar(models.Model):
	calender_name = models.CharField(max_length=50)
	source_name = models.CharField(max_length=50)
	user_email = models.EmailField()

	def __str__(self):
		return self.calendar_name