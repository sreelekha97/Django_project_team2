'''from django.forms import ModelForm

from .models import PersonalInfo

class RegistrationForm(ModelForm):

    class Meta:
        model = PersonalInfo
        fields = '__all__'
'''
from django import forms
from .models import Registration
from .models import PersonalInfo
from .models import AcademicInfo
from .models import AdditionalInfo

class RegForm(forms.ModelForm):

    class Meta:
        model = Registration
        fields = '__all__'
        

class PostForm(forms.ModelForm):

    class Meta:
        model = PersonalInfo
        fields = '__all__'
        

class AcadForm(forms.ModelForm):

    class Meta:
        model = AcademicInfo
        fields = '__all__'
        

class AddForm(forms.ModelForm):

    class Meta:
        model = AdditionalInfo
        fields = '__all__'
        

