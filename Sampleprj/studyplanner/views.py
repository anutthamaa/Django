from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
## functions and classes mapped to urls

def index(request):
    return HttpResponse('Welcome to Anu timetable')

def monday(request):
    return HttpResponse('Monday schedule is Deep learning')

def tuesday(request):
    return HttpResponse('Tuesday schedule is NLP')

def weeklySchedule(request,day):
    schedule = ''
    if day == "monday":
        schedule = 'Monday schedule : Deep learning'
    elif day == "tuesday":
        schedule = 'Tuesday schedule : NLP'
    elif day == "wednesday":
        schedule = 'Wednesday schedule : Machine Learning'
    elif day == "thursday":
        schedule = 'Thursday schedule : EDA'
    elif day == "friday":
        schedule = 'Friday schedule : Django/Flask'
    return HttpResponse(schedule)
    
