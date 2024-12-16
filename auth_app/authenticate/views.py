from django.shortcuts import render
from django.contrib.auth import authenticate, login ,logout

def home(reqeuest):
    return render(reqeuest, 'authenticate/home.html', {})

def login_user(request):
    return render(request, 'authenticate/login.html',{})