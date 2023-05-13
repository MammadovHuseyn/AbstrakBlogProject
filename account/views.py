from django.shortcuts import render , redirect
from django.contrib.auth import authenticate , login , logout
from django import forms

from core.tasks import send_welcome_mail
from .models import CustomUser
from .forms import RegisterForm , LoginForm
# Create your views here.

# def login_page(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']

#         user = authenticate(username = username, password = password)
#         if user is not None:
#             login(request, user)
#             return redirect('home_page')
#         else:
#             return render(request , 'account/login.html' , {'error': 'Username or password is incorrect!'})

#     return render(request , 'account/login.html')

def login_page(request):
    context = {
        'form' : LoginForm(),
    }
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username = username, password = password)
        if user is not None:
            login(request , user)
            return redirect('home_page')    
        else:
            context['error'] = 'Username or password is incorrect!'

    return render(request , 'account/login.html' , context)


def register_page(request):
    context = {
        'form' : RegisterForm()
    }
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            password = form.cleaned_data.get('password')
            repassword = form.cleaned_data.get('repassword')
            if password != repassword:
                context['error'] = 'Passwords do not match'
                context['form'] = form            
                return render(request , 'account/register.html' , context)
            
            user = form.save(commit=False)
            user.set_password(password)
            user.save()
            send_welcome_mail(email = user.email , username = f"{user.first_name} {user.last_name}")

            return redirect('login')
        else:
            context['form'] = form
    return render(request , 'account/register.html' , context)

    


def logout_request(request):
    logout(request)
    return redirect('home_page')