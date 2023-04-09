from django.db import models
from django.utils.text import slugify
from account.models import CustomUser
from ckeditor.fields import RichTextField

# Create your models here.

class Create(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True



class Blog(Create):
    title  = models.CharField(max_length=50)
    image = models.ImageField(upload_to='blogs')
    description = RichTextField()
    special_content = RichTextField(blank=True , null=True)
    category = models.ForeignKey("Category" ,on_delete=models.CASCADE, related_name='blog'  )
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE , related_name='blog' , blank=True)
  
    slug = models.SlugField(null=True , blank=True , unique= False , db_index= True , editable= True )

    def __str__(self):
        return self.title  
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Blog , self).save(*args, **kwargs)
    
    class Meta:
        verbose_name_plural = "Blogs"


class Comments(Create):
    writer = models.ForeignKey(CustomUser, on_delete = models.CASCADE , related_name= 'comments')
    blog = models.ForeignKey(Blog, on_delete = models.CASCADE , related_name='comments')
    comment_text = models.TextField()

    def __str__(self):
        return self.blog.title
    
    class Meta:
        verbose_name_plural = 'Comments'
    

class Category(Create):

    title = models.CharField(max_length=50)
    slug = models.SlugField(null=True , blank=True , unique= True , db_index= True , editable= False)

    def __str__(self):
        return self.title  
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "Categories"


class Contact(Create):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    company = models.CharField(max_length=100)
    text = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Contacts"

class Settings(models.Model):

    address = models.CharField(max_length=250 , null=True)
    phone1 = models.CharField(max_length=50, null=True)
    phone2 = models.CharField(max_length=50, null=True)
    email = models.EmailField(max_length=200 ,blank=True, null=True)

    facebook_url = models.URLField(max_length=200 , blank=True , null=True)
    instagram_url = models.URLField( max_length=200 , blank=True , null=True)
    twitter_url = models.URLField( max_length=200 , blank=True , null=True)
    linkedin_url = models.URLField( max_length=200 , blank=True , null=True)
    youtube_url = models.URLField( max_length=200 , blank=True , null=True)

    
    def __str__(self):
        return 'Settings'

    class Meta:
        verbose_name_plural =("Settings")