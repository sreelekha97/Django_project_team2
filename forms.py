'''from django.forms import ModelForm

from .models import PersonalInfo

class RegistrationForm(ModelForm):

    class Meta:
        model = PersonalInfo
        fields = '__all__'
'''
from django import forms

from .models import AcademicInfo

class PostForm(forms.ModelForm):

    class Meta:
        model = AcademicInfo
        fields = ('yearofjoining', 'currentsem', 'aggregate', 'institution','BoardofEducation','interagg', 'inst', 'BoardofEd', 'percent')
        


