from rest_framework import serializers
from .models import WorkoutModel

Workout = WorkoutModel

class WorkoutSerializers(serializers.ModelSerializer):
     exercise_name = serializers.CharField(max_length=100)
     sets = serializers.IntegerField()
     reps = serializers.IntegerField()
     weight_in_kg = serializers.IntegerField()

     class Meta():
          model = Workout
          fields = ['exercise_name', 'sets', 'reps', 'weight_in_kg']

     def create(self,validated_data):
          new_workout = Workout.objects.create(
               user=validated_data['user'],
               exercise_name=validated_data['exercise_name'],
               sets=validated_data['sets'],
               reps=validated_data['reps'],
               weight_in_kg=validated_data['weight_in_kg']
          ) 

          return new_workout
