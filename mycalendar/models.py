from django.db import models
import datetime

# Create your models here.

class CalendarEvent(models.Model):
	eventName = models.CharField(max_length = 128)
	eventDesc = models.CharField(max_length = 255)
	url = models.URLField()
	eventDate = models.DateField(editable = True)
	eventPriority = models.IntegerField(default = 1)

	def __str__(self):
		return self.eventName


