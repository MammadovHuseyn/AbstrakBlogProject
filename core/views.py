from django.shortcuts import render , get_object_or_404 , redirect
from .models import Blog , Category , Comments , Contact
from .forms import BlogForm , ContactForm , BlogUpdateForm
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

# Create your views here.

def home_page(request):

    return render(request , 'blog/index-1.html')



def blog_page(request, category_slug = None , blog_slug = None):
    #blogun detailine baxmiriqsa
    if blog_slug is None:           
        #eger blogu category filter elemiriyse
        if category_slug is not None:
            get_object_or_404(Category , slug=category_slug)             
            blogs = Blog.objects.filter(category__slug = category_slug)
        else:
            blogs = Blog.objects.order_by('-created_at')

            
        search_text = request.GET.get('search')
        if search_text:            
            blogs = Blog.objects.filter(title__icontains = search_text)
        
        categories = Category.objects.all()
        recentblogs = Blog.objects.order_by('-created_at')[:3]
        selected_category = category_slug

        #Pagination
        page = request.GET.get('page')
        if page is None:
            page = 1

        paginator = Paginator(blogs ,1)
        context = {
            'blogs':paginator.get_page(page),
            'categories': categories,
            'recentblogs': recentblogs,
            'selected_category': selected_category,
            'range' : range(1,int(paginator.num_pages)+1),
            'page': int(page)
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
            'blog' : blog,
            'categories' : categories,
            'comments': Comments.objects.filter(blog__slug=blog_slug),
            'selected_category': category_slug,
            'recentblogs': Blog.objects.order_by('-created_at')[:3],
            'related_blogs' : related_blogs,
        }
        return render(request , 'blog/single-blog.html' , context)


@login_required(login_url='login')
def personal_blog(request):
    context = {
        'blogs' : Blog.objects.filter(author = request.user),
        'categories': Category.objects.all(),
        'recentblogs': Blog.objects.order_by('-created_at')[:3],
    }
    if request.GET.get('search'):
        context['blogs'] = Blog.objects.filter(author= request.user , title__icontains = request.GET.get('search'))
    return render(request, 'blog/personalblog.html' , context)


@login_required(login_url='login')
def create_blog(request):

    context = {
        'categories': Category.objects.all(),
        'forms' : BlogForm(),
    }

    if request.method == 'POST':
        form = BlogForm(request.POST , request.FILES)
        if form.is_valid():            
            blog = form.save(commit=False)
            blog.author = request.user
            blog.save()
            form.save()
            return redirect('blog_page')
    else:
        form = BlogForm()
    return render(request, 'blog/addblog.html', context)

@login_required(login_url='login')
def update_blog(request , blog_slug):

    blog = get_object_or_404(Blog , slug=blog_slug ,author=request.user)
    form = BlogUpdateForm(request.POST or None , files=request.FILES or None , instance= blog)
    if request.method == 'POST':   
        if request.POST['btntitle'] == 'Delete':
            blog.delete()
            return redirect('blog_page')
   
    if form.is_valid():
        form.save()
        return redirect('blog_detail' , category_slug = blog.category.slug , blog_slug = blog.slug)

    context = {
        'forms' : form,
        'blog' : blog
    }
    return render(request, 'blog/updateblog.html', context)

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
