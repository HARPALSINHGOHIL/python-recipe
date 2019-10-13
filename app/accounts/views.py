from django.shortcuts import render, redirect
from django.contrib import messages


# Create your views here.
def register(request):
    if request.method == 'POST':
        messages.error(request, 'Testing Error message')
        return redirect('register')
    return render(request, 'accounts/register.html')


def login(request):
    if request.method == 'POST':
        print('SUBMITTED Login')
        return redirect('login')
    return render(request, 'accounts/login.html')


def logout(request):
    return redirect('index')


def dashboard(request):
    return render(request, 'accounts/dashboard.html')