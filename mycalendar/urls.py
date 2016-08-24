from django.conf.urls import url
from rest_framework.routers import DefaultRouter

from .views import ReminderViewSet, TaskViewSet, EventViewSet, CalendarViewSet

router = DefaultRouter()
router.register(r'^reminders', ReminderViewSet)
router.register(r'^tasks', TaskViewSet)
router.register(r'^events', EventViewSet)
router.register(r'^calendars', CalendarViewSet)

from . import views

urlpatterns = [
	url(r'^$', views.main, name="main"),
	url(r'^week$', views.week, name="week"),
]

urlpatterns += router.urls
