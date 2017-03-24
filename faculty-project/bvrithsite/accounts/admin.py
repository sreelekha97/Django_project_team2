from django.contrib import admin

# Register your models here.
from .models import Student
from .models import Faculty

admin.site.register(Faculty)
admin.site.register(Student)
