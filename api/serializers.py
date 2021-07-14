from rest_framework import fields, serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post 
        fields = ('id', 'heading', 'created_at', 'category', 'content')


class PostCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post 
        fields = ('heading', 'category', 'content')