from django.shortcuts import render
from .models import AcademicInfo
from .forms import PostForm
from django.http import HttpResponse
# Create your views here.

def register(request):
    return HttpResponse("Welcome to student info system")
def success(request):
    return HttpResponse("Succesfully Entered your details")

def post_new(request):
    if request.method=='GET':
       form = PostForm()
       return render(request, 'StudentDetails/register.html', {'form': form})
    elif request.method=='POST':
       form=PostForm(request.POST)
       if form.is_valid():
          AcademicInfo = form.save(commit=False)
          AcademicInfo.save()
          return success(form)

'''def index(request):
   details=PersonalInfo.objects.all()
   return render(request,'StudentDetails/index.html', {'details':details})
'''
'''def registrationform(request):
   form = RegistrationForm()
   if form.is_valid():
      PersonalInfo = form.save(commit=False)
      PersonalInfo .firstname = request.user
      PersonalInfo .secondname = request.user
      PersonalInfo .save()
   return render(request, 'StudentDetails/index.html', {'form': form})
'''

