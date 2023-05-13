from django.urls import path 
from .views import (
    BlogView , BlogDetailView , CommentView , CommentDeleteView, BlogCreateView , BlogUpdateView,
    BlogDeleteView , PostCommentView , PostCommentViewList , PostSubscriptionsView,
    PostCommentDeleteView
)

urlpatterns = [
    path('blog/'                            ,BlogView.as_view()                ,name = "blogapi" ),
    path('blog/detail/<int:id>/'            ,BlogDetailView.as_view()          ,name = "blogdetailapi" ),
    path('blog/create/'                     ,BlogCreateView.as_view()          ,name = "createapi" ),
    path('blog/update/<int:id>/'            ,BlogUpdateView.as_view()          ,name = "blogupdateapi" ),
    path('blog/delete/<int:id>/'            ,BlogDeleteView.as_view()          ,name = "deleteblog" ),

    path('comment/'                         ,CommentView.as_view()             ,name = "blog_comment_create" ),
    path('comment/delete/<int:id>/'         ,CommentDeleteView.as_view()       ,name = "blog_comment_delete" ),

    path('postcomment/'                     ,PostCommentView.as_view()         ,name = "post_comment_create" ),
    path('post/comments/'                   ,PostCommentViewList.as_view()     ,name = "post_comment_list"),
    path('post/comment/delete/<int:id>/'    ,PostCommentDeleteView.as_view()   ,name = "post_comment_delete" ),

    path('subscribe/'                       ,PostSubscriptionsView().as_view() ,name = "subscribe"),

]
