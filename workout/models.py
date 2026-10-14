from django.db import models
from django.conf import settings

# Create your models here.
class WorkoutModel(models.Model):
     user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='workout')
     exercise_name = models.CharField(max_length=100)
     sets = models.IntegerField()
     reps = models.IntegerField()
     weight_in_kg = models.IntegerField()
     created_at = models.DateField(auto_now_add=True)

     def __str__(self) -> str:
          return f"{self.user.username}"
     