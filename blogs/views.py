from django.shortcuts import render
from rest_framework import generics, status, permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Blog
from .serializers import BlogSerializer

# Create your views here.

class PostCreateView(generics.CreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [permissions.IsAuthenticated, ]


class PostListView(generics.ListAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [permissions.IsAuthenticated, ]



@api_view(['POST'])
def post_like(request, pk):
    post = Blog.objects.get(pk=pk)
    post.likes += 1
    post.save()
    serializer = BlogSerializer(post)
    permission_classes = [permissions.IsAuthenticated, ]
    return Response(serializer.data)