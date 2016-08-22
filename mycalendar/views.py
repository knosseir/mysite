from django.shortcuts import render

from rest_framework import viewsets

# Create your views here.
def main(request):
	return render(request, 'mycalendar/main.html')