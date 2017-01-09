from django.db import models

# Create your models here.

from django.db import models
from django.utils import timezone


class Student(models.Model):
    student = models.ForeignKey('auth.User')
    name = models.CharField(max_length=200)
    branch = models.CharField(max_length=200)
    marks = models.IntegerField()
    year = models.IntegerField()
    created_date = models.DateTimeField(
            default=timezone.now)
    updated_date = models.DateTimeField(
            blank=True, null=True)

    def update(self):
        self.updated_date = timezone.now()
        self.save()


    def __str__(self):
        return self.name
