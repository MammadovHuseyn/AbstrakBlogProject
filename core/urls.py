from django.urls import path , include
from .views import home_page , blog_page , personal_blog , create_blog , contact , update_blog


urlpatterns = [
    path('' , home_page , name = 'home_page'),

    path('blog/' , blog_page , name = 'blog_page'),
    path('blog/<slug:category_slug>/' , blog_page , name = 'blog_category'),
    path('blog/<slug:category_slug>/<slug:blog_slug>/' , blog_page , name = 'blog_detail'),
    path('personal/' , personal_blog , name = 'blog_personal'),
    path('addblog/' , create_blog , name='addblog'),
    path('contact/' , contact , name='contact_page'),
    path('update-blog/<slug:blog_slug>' , update_blog , name='update_blog'),
]

# 