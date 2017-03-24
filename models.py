from django.db import models
from django.utils import timezone

# Create your models here.
class AcademicInfo(models.Model):
   yearofjoining = models.DateTimeField(blank=True, null=True)
   currentsem = models.CharField(max_length=8)
   aggregate = models.CharField(max_length=10)
   institution = models.CharField(max_length=200)
   BoardofEducation = models.CharField(max_length=10)
   interagg = models.CharField(max_length=10)
   inst = models.CharField(max_length=200)
   BoardofEd = models.CharField(max_length=10)
   percent = models.CharField(max_length=10)

   def __str__(self):
      return self.yearofjoining
