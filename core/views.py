from django.shortcuts import render , get_object_or_404 , redirect
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.hashers import check_password

from account.models import CustomUser
from account.forms import UpdateProfileForm , UpdatePasswordForm

from core.models import Blog , Category , Comments , Contact , Post , PostComments , Services , Services_category
from core.forms import PostForm , ContactForm , BlogUpdateForm
from core.tasks import send_mail_to_Contact

from random import choice ,choices

def home_page(request):
    posts = Post.objects.filter(is_active=True).order_by("-created_at")[:3]

    context = {
        "blogs" : Blog.objects.filter(is_active=True).order_by("-created_at")[:2],
        "posts" : posts,
        "users" : CustomUser.objects.all().count(),
        "services":Services.objects.all().order_by("-created_at")[:6],

    }
    
    return render(request , 'blog/homepage.html' , context)

def service_page(request):
    context = {
        "services" : Services.objects.all(),
        "cats" : Services_category.objects.all()
    }
    return render(request , 'blog/service.html' , context)

def service_detail(request , service_slug):
    service = get_object_or_404(Services, slug=service_slug)
    context = {
        "service" : service,
    }
    return render(request, "blog/service_detail.html", context)

def profile_edit(request):
    user = request.user
    form = UpdateProfileForm(instance=user)
    password_form = UpdatePasswordForm()    

    context = {
        "forms": form,
        "password_form": password_form,
    }
    if request.method == 'POST':

        if request.POST.get('value') == 'profile':
            form = UpdateProfileForm(request.POST , request.FILES , instance= user)
            if form.is_valid():

                username = form.cleaned_data["username"]
                first_name = form.cleaned_data["first_name"]
                last_name = form.cleaned_data["last_name"]
                avatar = form.cleaned_data['avatar']
                email = form.cleaned_data["email"]
                bio = form.cleaned_data["bio"]
                
                if request.user.username != username :
                    if CustomUser.objects.filter(username = username).exists():
                        pass
                    else:
                        user.username = form.cleaned_data['username']
                                           

                if not CustomUser.objects.filter(email = email).count() > 1:
                    user.email = form.cleaned_data['email']
                
                user.first_name = first_name
                user.last_name = last_name
                user.avatar = avatar
                user.bio = bio

                user.save()
                context["forms"] = UpdateProfileForm(instance= user)

                return render(request, 'blog/profile.html',context)

        if request.POST.get('value') == 'password':
            password_form = UpdatePasswordForm(request.POST)
            if password_form.is_valid():
                newpassword = password_form.cleaned_data['newpassword']
                repassword = password_form.cleaned_data['repassword']
                oldpassword = password_form.cleaned_data['oldpassword']
                if newpassword == repassword:

                    if check_password(oldpassword,user.password ):

                        user.set_password(newpassword)
                        user.save()
                        return redirect("login")
                    else:
                        context['error'] = "Old password do not match"
                else:
                    context["error"] = "Passwords do not match"  

    context["user"] = user

    return render(request, 'blog/profile.html',context)

def blog_page(request, blog_slug = None):

    if blog_slug is None:           
        blogs       = Blog.objects.order_by('-created_at')            
        search_text = request.GET.get('search')
        category    = request.GET.get('cat')
        startdate   = request.GET.get('startdate')
        enddate     = request.GET.get('enddate')

        if search_text and (startdate or enddate) and category: 
             blogs = Blog.objects.filter(
                Q(title__icontains = search_text) | Q(description__icontains = search_text),
                created_at__range = [startdate, enddate] , category__id = category           
            )
        elif search_text:
            blogs =Blog.objects.filter(Q(title__icontains = search_text) | Q(description__icontains = search_text))

        elif startdate or enddate:
            blogs = Blog.objects.filter(created_at__range = [startdate, enddate])

        elif category:
            blogs = Blog.objects.filter(category__id = category)

        elif search_text and (startdate or enddate):
            blogs = Blog.objects.filter(Q(title__icontains = search_text) | Q(description__icontains = search_text , created_at__range = [startdate, enddate]))

        elif search_text and category:
            blogs = Blog.objects.filter(Q(title__icontains = search_text) | Q(description__icontains = search_text , category__id = category))

        elif category and (startdate or enddate):
            blogs = Blog.objects.filter(category__id = category , created_at__range = [startdate, enddate])
        
        if category == "":
            category = None
        
        categories = Category.objects.all()
        recentblogs = Blog.objects.order_by('-created_at')[:3]

        #Pagination
        page = request.GET.get('page')
        if page is None:
            page = 1

        paginator = Paginator(blogs ,3)
        context = {
            'blogs'      : paginator.get_page(page),
            'blog_count' : blogs.count(),
            'categories' : categories,
            'recentblogs': recentblogs,
            'range'      : range(1,int(paginator.num_pages)+1),
            'page'       : int(page),
            'search_text': search_text,
            'category'   : Category.objects.filter(id = category).first(),
            'start_date' : startdate,
            'end_date'   : enddate,
        }

        return render(request , 'blog/blog.html' , context)

    else:        
        get_object_or_404(Blog , slug=blog_slug)
        blog = Blog.objects.get(slug = blog_slug)
        categories = Category.objects.all()
        related_blogs = Blog.objects.filter(category= blog.category)
        
        if request.method == 'POST':
            comment = Comments()
            comment.comment_text = request.POST['message']
            comment.writer = request.user
            comment.blog = Blog.objects.get(slug = blog_slug)
            comment.save()
            
        context = {
            'blog'             : blog,
            'categories'       : categories,
            'comments'         : Comments.objects.filter(blog__slug=blog_slug),
            'recentblogs'      : Blog.objects.order_by('-created_at')[:3],
            'related_blogs'    : related_blogs,
        }
        return render(request , 'blog/blog_detail.html' , context)


@login_required(login_url='login')
def my_posts(request , username):
    context = {
        'posts' : Post.objects.filter(author = CustomUser.objects.get(username=username) , is_active=True),
    }
    if request.GET.get('search'):
        context['posts'] = Post.objects.filter(author = CustomUser.objects.get(username=username) , title__icontains = request.GET.get('search'))
        if context['posts'].count() == 0:
            context['msg'] = 'No blog found'
    return render(request, 'blog/my_posts.html' , context)


@login_required(login_url='login')
def create_post(request):

    context = {
        'categories': Category.objects.all(),
        'form' : PostForm(),
    }

    if request.method == 'POST':
        form = PostForm(request.POST , request.FILES)
        if form.is_valid():            
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            form.save()

            return redirect('post_page')
    else:
        context["form"] = PostForm(request.POST , request.FILES)
    return render(request, 'blog/post_share.html', context)

@login_required(login_url='login')
def post_update(request , blog_slug):

    post = get_object_or_404(Post , slug=blog_slug ,author=request.user)
    form = BlogUpdateForm(request.POST or None , files=request.FILES or None , instance= post)
    if request.method == 'POST':   
        if request.POST['btntitle'] == 'Delete':
            post.delete()
            return redirect('post_page')
        if request.POST['btntitle'] == 'image':
            post.image.delete()
            post.save()
            return redirect('post_page')
   
    if form.is_valid():
        form.save()
        return redirect('post_detail', post_slug = post.slug)

    context = {
        'forms' : form,
        'blog' : post
    }
    return render(request, 'blog/post_update.html', context)

@login_required(login_url='login')
def contact(request):

    context = {
        'forms' : ContactForm()
    }

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            
    return render(request, 'blog/contact.html' , context)


def post_page(request):

    posts = Post.objects.filter(is_active=True)

    page = request.GET.get('page')
    if page is None:
        page = 1

    paginator = Paginator(posts ,10)

    context = {
        "posts": paginator.get_page(page),
        "post_count": posts.count(),
        'range'      : range(1,int(paginator.num_pages)+1),
        'page'       : int(page),
    }

    return render(request, 'blog/post_page.html' ,context)

def post_detail(request , post_slug):

    post = get_object_or_404(Post , slug=post_slug)
    context = {
        "post": post,
        "comments" : PostComments.objects.filter(post=post).all(),
    }
    return render(request, 'blog/post_detail.html', context)

def profile_detail(request , username):
    user = CustomUser.objects.filter(username=username).first()

    context = {
        "user": user,
    }
    return render(request, 'blog/profile_detail.html' , context)
