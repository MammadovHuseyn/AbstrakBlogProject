from django import forms
from .models import Blog , Contact

class BlogForm(forms.ModelForm):
     class Meta:
        model = Blog
        fields = ['title' ,  'description', 'special_content','image', 'category',]
        widgets ={
            'title': forms.TextInput(attrs={'class':"form-control", 'name':"title", 'placeholder':'Blog Name'}),
            'image' : forms.FileInput(attrs={'type':"file", 'name':"image" }),
            'description' : forms.Textarea(attrs={'name':"description", 'class':"form-control textarea", 'cols':"40", 'rows':"4" , 'placeholder':'Description'}),
            'category' : forms.Select(attrs={'name':"category", 'class':"form-control"}),
            'special_content' : forms.Textarea(attrs={'name':"special_content", 'class':"form-control textarea", 'cols': "40" , 'rows': "4" , 'placeholder':'Special Content'}),
            
        }


class BlogUpdateForm(forms.ModelForm):
    # title = forms.CharField(widget=forms.TextInput(attrs={'class':"form-control", 'name':"title", 'placeholder':'Blog Name'}))
    # image = forms.ImageField(widget=forms.FileInput(attrs={'type':"file", 'name':"image" }))
    # description = forms.CharField(widget=forms.Textarea(attrs={'name':"description", 'class':"form-control textarea", 'cols':"30", 'rows':"4"}))
    # category = forms.ChoiceField(widget=forms.Select(attrs={'name':"category", 'class':"form-control"}))
       class Meta:
        model = Blog
        fields = ['title' ,  'description', 'special_content','image', 'category']
        widgets ={
            'title': forms.TextInput(attrs={'class':"form-control", 'name':"title", 'placeholder':'Blog Name'}),
            'image' : forms.FileInput(attrs={'type':"file", 'name':"image" }),
            'description' : forms.Textarea(attrs={'name':"description", 'class':"form-control textarea", 'cols':"30", 'rows':"4"}),
            'category' : forms.Select(attrs={'name':"category", 'class':"form-control"}),
            'special_content' : forms.Textarea(attrs={'name':"special_content", 'class':"form-control textarea", 'cols': "30" , 'rows': "4"}),
        }
    


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('name', 'email', 'company', 'text')
        widgets = {
            'name' : forms.TextInput(attrs={'type':"text", 'name':"contact_name", 'class':"form-control" , 'placeholder':'Enter name'}),
            'email': forms.EmailInput(attrs={'type':"email" , 'class':"form-control" , 'name' : 'contact-email' , 'placeholder':'Enter email'}),
            'company': forms.TextInput(attrs={'type':"text" , 'class':"form-control" , 'name' : 'contact-company' , 'placeholder':'Enter company'}),
            'text' : forms.Textarea(attrs={'class':"form-control textarea" , 'name':'contact-message', 'id':'contact-message','cols':"30" , 'rows' : '4'})
        }

