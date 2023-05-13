from rest_framework import serializers

from core.models import Blog , Comments , PostComments  ,Subscription

class BlogSerializer(serializers.ModelSerializer):

    class Meta:
        model = Blog
        fields = ['title', 'description', 'image', 'category', 'created_at']


class BlogPostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Blog
        fields = ['author', 'title', 'description', 'image', 'category']



class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comments
        fields = ['writer' , "blog" , "comment_text"]


class PostCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostComments
        fields = ['writer' , "post" , "comment_text"]


class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = ["email",]