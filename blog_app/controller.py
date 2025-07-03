from .models import Blog_Post
from .serializers import Post_Serializer
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

class PostController:

    @staticmethod
    def create_post(request):
        add_post = Post_Serializer(data=request.data)
        if add_post.is_valid():
            add_post.save()
            return Response({"message" : "New Post Created!"})
        return Response(add_post.errors)

    @staticmethod
    def get_posts(post_id=None):
        if post_id is None:
            posts = Blog_Post.objects.all()
            serialized = Post_Serializer(posts, many=True)
            return Response(serialized.data)
        post = get_object_or_404(Blog_Post, id=post_id)
        serialized = Post_Serializer(post)
        return Response(serialized.data)

    @staticmethod
    def update_post(request, post_id):
        post = get_object_or_404(Blog_Post, id=post_id)
        serializer = Post_Serializer(post, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"message":"Task Updated!"})
        return Response(serializer.errors)

    @staticmethod
    def delete_post(post_id):
        post = get_object_or_404(Blog_Post, id=post_id)
        post.delete()
        return Response({"message":"Post was Deleted!"})
