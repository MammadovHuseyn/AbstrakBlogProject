from django.shortcuts import render , redirect
from django.contrib.auth import authenticate , login , logout
from .models import CustomUser
from .forms import RegisterForm , LoginForm
from django import forms
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

            form.save()
            return redirect('login')
        else:
            context['form'] = form
    return render(request , 'account/register.html' , context)

    


def logout_request(request):
    logout(request)
    return redirect('home_page')