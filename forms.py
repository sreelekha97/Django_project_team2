'''from django.forms import ModelForm

from .models import PersonalInfo

class RegistrationForm(ModelForm):

    class Meta:
        model = PersonalInfo
        fields = '__all__'
'''
from django import forms

from .models import PersonalInfo

class PostForm(forms.ModelForm):

    class Meta:
        model = PersonalInfo
        fields = ('rollno', 'firstname', 'lastname', 'email','phonenumber','dob','address')
        

