from django.urls import path
from . import views


###local:8000/studyplanner/index
urlpatterns = [
    path('index', views.index),
    ###path('monday', views.monday),
    path('<day>', views.weeklySchedule)
    
    ]