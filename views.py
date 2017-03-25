from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, render_to_response
from .models import Registration
from .models import PersonalInfo
from .models import AcademicInfo
from .models import AdditionalInfo
from .forms import RegForm
from .forms import PostForm
from .forms import AcadForm
from .forms import AddForm


def register(request):
    if request.method == "POST":
        form = RegForm(request.POST)
        if form.is_valid():       
            Registration = form.save(commit = True)
            Registration.save()           
            return redirect('perInfo')
       
    else:
        form = RegForm()
    return render(request, "StudentDetails/register.html", {'form': form})


def perInfo(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():       
            PersonalInfo = form.save(commit = False)
            PersonalInfo.save()           
            return redirect('acadInfo')
       
    else:
        form = PostForm()
    return render(request, "StudentDetails/perInfo.html", {'form': form})

def acadInfo(request):
    if request.method == "POST":
        form = AcadForm(request.POST)
        if form.is_valid():       
            AcademicInfo = form.save(commit = False)
            AcademicInfo.save()           
            return redirect('addInfo')
       
    else:
        form = AcadForm()
    return render(request, "acad.html", {'form': form})

def addInfo(request):
    if request.method == "POST":
        form = AddForm(request.POST)
        if form.is_valid():       
            AdditionalInfo = form.save(commit = False)
            AdditionalInfo.save()           
            return redirect('display')
       
    else:
        form = AddForm()
    return render(request, "add.html", {'form': form})

'''def success(request):
            try:
                drive_details = AdditionalInfo.objects.all()
            except AdditionalInfo.DoesNotExist:
                raise Http404("DriveDetails does not exist")
            return render(request, 'viewDrives.html', {'drive_details': drive_details})
'''           
def display(request):
            try:
                login_details = Registration.objects.all()
                perInfo_details = PersonalInfo.objects.all()
                acadInfo_details = AcademicInfo.objects.all()
                addInfo_details = AdditionalInfo.objects.all()
            except PersonalInfo.DoesNotExist:
                raise Http404("Comment does not exist")
            return render(request, "display.html",{'login_details': login_details, 'perInfo_details': perInfo_details, 'acadInfo_details':acadInfo_details, 'addInfo_details':addInfo_details})


