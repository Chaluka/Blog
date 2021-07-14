from django.shortcuts import render
from rest_framework import generics, serializers, status
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Post
from .serializers import PostSerializer, PostCreateSerializer


class PostView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
 

class CreatePostView(APIView):
    serializer_class = PostCreateSerializer

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            heading = serializer.data.get('heading')
            category = serializer.data.get('category')
            content = serializer.data.get('content')
            post = Post(heading=heading, category=category, content=content)
            post.save()
            return Response(PostSerializer(post).data, status=status.HTTP_201_CREATED)

        return Response({'Bad Request': 'Invalid data...'}, status=status.HTTP_400_BAD_REQUEST)