from django.forms import ModelForm
from account.models import CustomUser
from django import forms


class RegisterForm(ModelForm):

    repassword = forms.CharField(widget = forms.PasswordInput(attrs={'type': 'password' , 'placeholder':'Enter your repassword', 'name':'repassword'}))
    
    class Meta:
        model = CustomUser
        fields = ['username','email','first_name','last_name','password','repassword']
        widgets = {
            'username' : forms.TextInput(attrs={'type':'text', 'placeholder':'Enter your username','name':'username'}),
            'email' : forms.TextInput(attrs={'type':'email', 'placeholder':'Enter your email address','name':'email'}),
            'first_name' : forms.TextInput(attrs={'type':'text', 'placeholder':'Enter your first name','name':'firstname'}),
            'last_name' : forms.TextInput(attrs={'type':'text', 'placeholder':'Enter your last name','name':'lastname'}),
            'password' : forms.PasswordInput(attrs={'type':'password', 'placeholder':'Enter your password' , 'name':'password' }),
        }
    
    def clean(self):
        
        password = self.cleaned_data['password']
        repassword = self.cleaned_data['repassword']
        if password != repassword:
            raise forms.ValidationError('Passwords do not match')


    def clean_password(self):
        password = self.cleaned_data['password']
        if len(password) < 8:
            raise forms.ValidationError('Password must be bigger than 8 characters')
        else:
            if all(c.isdigit() for c in password):
                raise forms.ValidationError('Password cannot contain digits')
        return password
        
    def clean_email(self):
        email = self.cleaned_data['email']
        if CustomUser.objects.filter(email=email).exists():
            raise forms.ValidationError('Email address already in use')
        
        return email

    def clean_usernames(self):
        username = self.cleaned_data['username']
        if CustomUser.objects.filter(username=username).exists():
            raise forms.ValidationError('This username already in use')

    
    

    

class LoginForm(forms.Form):
    username = forms.CharField(widget= forms.TextInput(attrs={'type':'text', 'placeholder':'Enter your username','name':'username'}))
    password = forms.CharField(widget= forms.PasswordInput(attrs={'type':'password', 'placeholder':'Enter your password' , 'name':'password' }))
  