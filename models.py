from django.db import models
from django.utils import timezone

# Create your models here.
class PersonalInfo(models.Model):
   rollno = models.CharField(max_length=30)
   firstname = models.CharField(max_length=30)
   lastname = models.CharField(max_length=30)
   email = models.CharField(max_length=30)
   phonenumber = models.CharField(max_length=10)
   dob = models.DateTimeField(blank=True, null=True)
   address = models.CharField(max_length=70)

   def __str__(self):
      return self.rollno

