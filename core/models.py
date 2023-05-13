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
    category = models.ForeignKey("Category" ,on_delete=models.CASCADE, related_name='blog')
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE , related_name='blog')
    reading_time = models.IntegerField(default=0)
    is_active = models.BooleanField(default= True)
    slug = models.SlugField(null=True , blank=True , unique= False , db_index= True , editable= False )

    def __str__(self):
        return self.title  
    
    def save(self, *args, **kwargs):
        from core.tasks import send_mail_to_Contact
        self.slug = slugify(self.title)
        if Blog.objects.filter(slug=self.slug).exists():
            self.slug = self.slug + "-" + str(Blog.objects.filter(slug=self.slug).count())
        
        if not Blog.objects.filter(slug=self.slug).exists():
            send_mail_to_Contact.delay()
        super(Blog , self).save(*args, **kwargs)
    
    class Meta:
        verbose_name_plural = "Blogs"

class Services(Create):
    title  = models.CharField(max_length=50)
    image = models.ImageField(upload_to='services')
    description = RichTextField()
    slug = models.SlugField(null=True , blank=True , unique= False , db_index= True , editable= False )
    category = models.ForeignKey("Services_category", blank=True , null=True , related_name="services" , on_delete = models.CASCADE)
    def __str__(self):
        return self.title  
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        if Services.objects.filter(slug=self.slug).exists():
            self.slug = self.slug + "-" + str(Services.objects.filter(slug=self.slug).count())

        super(Services , self).save(*args, **kwargs)  
    
    class Meta:
        verbose_name_plural = "Services"

class Services_category(models.Model):
    title  = models.CharField(max_length=50)

    def __str__(self):
        return self.title  
    
    class Meta:
        verbose_name_plural = "Services Category"

class Comments(Create):
    writer = models.ForeignKey(CustomUser, on_delete = models.CASCADE , related_name= 'comments')
    blog = models.ForeignKey(Blog, on_delete = models.CASCADE , related_name='comments')
    comment_text = models.TextField()

    def __str__(self):
        return self.blog.title
    
    class Meta:
        verbose_name_plural = 'Comments'

class PostComments(Create):
    writer = models.ForeignKey(CustomUser, on_delete = models.CASCADE , related_name= 'post_comments')
    post = models.ForeignKey("Post", on_delete = models.CASCADE , related_name='post_comments')
    comment_text = models.TextField()

    def __str__(self):
        return self.post.title
    
    class Meta:
        verbose_name_plural = 'Post Comments'


class Post(Create):
    title  = models.CharField(max_length=120)
    image = models.ImageField(upload_to='posts' , blank= True)
    description = RichTextField()
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE , related_name='post' , blank=True , null = True)
    is_active = models.BooleanField(default= True)
    slug = models.SlugField(null=True , blank=True , unique= False , db_index= True , editable= False )

    def __str__(self):
        return self.title  
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        if Post.objects.filter(slug=self.slug).exists():
            self.slug = self.slug +"-"+ str(Post.objects.filter(slug=self.slug).count())

        super(Post , self).save(*args, **kwargs)
    
    class Meta:
        verbose_name_plural = "Posts"
    

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


class Subscription(models.Model):
    email = models.EmailField( max_length=254)

    def __str__(self):
        return self.email

    class Meta:
        verbose_name_plural =("Subscription")