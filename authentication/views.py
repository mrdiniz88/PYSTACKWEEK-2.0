from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.messages import constants
from django.contrib import messages
from django.contrib import auth

def register(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect('/')
        return render(request, 'register.html')
    elif request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        if len(username.strip()) == 0 or len(email.strip()) == 0 or len(password.strip()) == 0:
            messages.add_message(request, constants.ERROR, 'Fill in all fields')
            return redirect('/auth/register')
        
        user = User.objects.filter(username=username)
        
        if user.exists():
            messages.add_message(request, constants.ERROR, 'user already exists')
            return redirect('/auth/register')
        
        try:
            user = User.objects.create_user(username=username, email=email, password=password)
        
            user.save()
            messages.add_message(request, constants.SUCCESS, 'Successful registration')
            return redirect('/auth/login')
        except:
            messages.add_message(request, constants.ERROR, 'Internal error')
            return redirect('/auth/register')
        
def login(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            return redirect('/')
        return render(request, 'login.html')
    elif request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        usuario = auth.authenticate(username=username, password=password)
        if not usuario:
            messages.add_message(request, constants.ERROR, 'Invalid username or password')
            return redirect('/auth/login')
        else:
            auth.login(request, usuario)
            return redirect('/')


def logout(request):
    auth.logout(request)
    return redirect('/auth/login')