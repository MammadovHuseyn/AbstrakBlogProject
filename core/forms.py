from django import forms
from .models import Blog , Contact , Post
from ckeditor.widgets import CKEditorWidget

class PostForm(forms.ModelForm):
     class Meta:
        model = Post
        fields = ['title' , 'description','image', ]
        widgets ={
            'title'       : forms.TextInput(attrs={'class':"form-control", 'name':"title", 'placeholder':'Post Name' , "style":"margin-bottom:10px"}),
            'description' : forms.Textarea(attrs={'name':"description", 'class':"form-control" , 'placeholder':'Description' , 'style':"width:100","style":"margin-bottom:20px"}),
            'image'       : forms.FileInput(attrs={'type':"file", 'name':"image" }),

            
        }


class BlogUpdateForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['title', 'description','image']
        widgets ={
            'title'       : forms.TextInput(attrs={'class':"form-control", 'name':"title", 'placeholder':'Post Name'}),
            'image'       : forms.FileInput(attrs={'type':"file", 'name':"image" }),
            'description' : forms.Textarea(attrs={'name':"description", 'class':"form-control textarea", 'cols':"30", 'rows':"4"}),
        }
    


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('name', 'email', 'company', 'text')
        widgets = {
            'name'      : forms.TextInput(attrs={'type':"text", 'name':"contact_name", 'class':"form-control" , 'placeholder':'Enter name'}),
            'email'     : forms.EmailInput(attrs={'type':"email" , 'class':"form-control" , 'name' : 'contact-email' , 'placeholder':'Enter email'}),
            'company'   : forms.TextInput(attrs={'type':"text" , 'class':"form-control" , 'name' : 'contact-company' , 'placeholder':'Enter company'}),
            'text'      : forms.Textarea(attrs={'class':"form-control textarea" , 'name':'contact-message', 'id':'contact-message','cols':"30" , 'rows' : '4'})
        }

