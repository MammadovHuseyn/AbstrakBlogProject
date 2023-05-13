from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListAPIView , CreateAPIView , DestroyAPIView , RetrieveAPIView , UpdateAPIView


from core.models import Blog , PostComments , Comments , Subscription
from .serializer import BlogSerializer , BlogPostSerializer , CommentSerializer , PostCommentSerializer , SubscriptionSerializer
# Create your views here.

### Get all blogs
class BlogView(ListAPIView):
    queryset = Blog.objects.filter(is_active=True)
    serializer_class = BlogSerializer

### Blog detail api
class BlogDetailView(RetrieveAPIView):
    queryset = Blog.objects.filter(is_active=True)
    serializer_class = BlogSerializer
    lookup_field = "id"

### Post a new blog
class BlogCreateView(CreateAPIView):
    queryset = Blog.objects.filter(is_active=True)
    serializer_class = BlogPostSerializer

    # Set Request User to the Author
    def perform_create(self, serializer):
        serializer.save(author = self.request.user)

### Blog Update API
class BlogUpdateView(UpdateAPIView):
    queryset = Blog.objects.filter(is_active=True)
    serializer_class = BlogSerializer
    lookup_field = "id"
    
### Blog Delete API
class BlogDeleteView(DestroyAPIView):
    queryset = Blog.objects.filter(is_active= True )
    serializer_class = BlogSerializer
    lookup_field = "id"



# ##############################################################################

# class BlogView(APIView):
    
#     def get(self, request):
#         blogs = Blog.objects.filter(is_active= True)
#         serializer = BlogSerializer(blogs , many = True , context = {"request" : request })
#         return Response(serializer.data , status = status.HTTP_200_OK)

#     def post(self, request):
#         serializer = BlogPostSerializer(data= request.data , context = {"request" : request})
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data , status = status.HTTP_201_CREATED)

#         else:
#             return Response(serializer.errors , status = status.HTTP_400_BAD_REQUEST)



# class BlogDetailView(APIView):

#     def get(self, request , id):
#         try:
#             blog = Blog.objects.get(id=id)
#             serializer = BlogSerializer(blog , context = {"request" : request})
#             return Response(serializer.data , status = status.HTTP_200_OK)

#         except Blog.DoesNotExist:
#             return Response(status = status.HTTP_404_NOT_FOUND , data = {"message" : "Blog not found"})

#     def put(self, request , id):
#         try:
#             blog = Blog.objects.get(id=id)
#             serializer = BlogPostSerializer(blog , data= request.data , context = {"request" : request})
#             if serializer.is_valid():
#                 serializer.save()
#                 return Response(serializer.data , status = status.HTTP_200_OK)
#             else: 
#                 return Response(status = status.HTTP_400_BAD_REQUEST)

#         except Blog.DoesNotExist:
#             return Response(status = status.HTTP_404_NOT_FOUND , data = {"message" : "Blog not found"})


class CommentView(APIView):

    def post(self, request):
        serializer = CommentSerializer(data= request.data , context = {"request" : request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data , status = status.HTTP_201_CREATED)

        else:
            return Response(serializer.errors , status = status.HTTP_400_BAD_REQUEST)

### Comment Delete API
class CommentDeleteView(DestroyAPIView):
    queryset = Comments.objects.all()
    serializer_class = CommentSerializer()
    lookup_field = "id"

class PostCommentDeleteView(DestroyAPIView):
    queryset = PostComments.objects.all()
    serializer_class = PostCommentSerializer()
    lookup_field = "id"


class PostCommentViewList(ListAPIView):
    queryset = PostComments.objects.all()
    serializer_class = PostCommentSerializer


class PostCommentView(APIView):

    def post(self, request):
        serializer = PostCommentSerializer(data= request.data , context = {"request" : request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data , status = status.HTTP_201_CREATED)

        else:
            return Response(serializer.errors , status = status.HTTP_400_BAD_REQUEST)

### Subscriptions api
class PostSubscriptionsView(CreateAPIView):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer
