from django.urls import path , include

from .views import (

home_page , blog_page , post_page , post_detail, my_posts ,
create_post , contact , post_update , profile_edit , profile_detail,
service_page , service_detail

)


urlpatterns = [
#  | URLs |                             | Functions |    | URL names |

    path(''                             ,home_page      ,name = 'home_page'),

    path('blog/'                        ,blog_page      ,name = 'blog_page'),
    path('blog/<slug:blog_slug>/'       ,blog_page      ,name = 'blog_detail'),

    path('post/'                        ,post_page      ,name = 'post_page'),
    path('post/<slug:post_slug>'        ,post_detail    ,name = 'post_detail'),
    path('share/'                       ,create_post    ,name = 'create_post'),
    path('update-post/<slug:blog_slug>' ,post_update    ,name = 'update_blog'),
    path('personal/<str:username>'      ,my_posts       ,name = 'my_posts'),

    path('profile/<str:username>'       ,profile_detail ,name = 'profile'),
    path('profile/'                     ,profile_edit   ,name = 'profile_edit'),
    
    path('service/<slug:service_slug>'  ,service_detail ,name = 'service_detail'),
    path('services/'                    ,service_page   ,name = 'service_page'),

    path('contact/'                     ,contact        ,name = 'contact_page'),
]

