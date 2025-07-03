from rest_framework import serializers
from .models import Blog_Post

class Post_Serializer(serializers.ModelSerializer):
    
    created_at = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S', read_only=True)

    class Meta:

        model = Blog_Post
        fields = ['id','title', 'content', 'created_at', 'author',]