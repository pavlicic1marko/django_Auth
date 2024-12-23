from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login ,logout
from django.contrib import messages

def home(reqeuest):
    return render(reqeuest, 'authenticate/home.html', {})

def logout_user(request):
    logout(request)
    messages.success(request, ('You Have Been Logged Out...'))
    return redirect('home')

def login_user(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request,('You Have been logged in!'))
            return redirect('home')
        else:
            messages.error(request,('Error'))
            return redirect('login')
    else:
        return render(request, 'authenticate/login.html',{})


