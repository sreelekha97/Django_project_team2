from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>Login</h1><form>username:<br><input type='text' name='username' ><br>password:<br><input type='password' name='password'><br><br><input type='submit' value='Submit'></form> ")
