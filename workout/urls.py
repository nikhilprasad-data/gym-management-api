from django.urls import path
from .views import create_workout_view

urlpatterns = [
     path('create/', create_workout_view, name= 'create_workout_view'),
]