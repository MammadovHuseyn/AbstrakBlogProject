from django.urls import path , include
from .views import login_page , register_page , logout_request


urlpatterns = [

    path('login/' , login_page , name = 'login'),
    path('register/' , register_page , name = 'register'),
    path('logout/' , logout_request , name = 'logout'),


]
