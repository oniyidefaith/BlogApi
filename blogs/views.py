from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import generics, status, permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Blog
from .serializers import BlogSerializer
from rest_framework.pagination import PageNumberPagination

# Create your views here.

class PostCreateView(generics.CreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [permissions.IsAuthenticated, ]


class PostListView(generics.ListAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [permissions.IsAuthenticated, ]


class BlogListAPIView(APIView):
    permission_classes = [permissions.AllowAny]
    pagination_class = PageNumberPagination

    def get(self, request):
        blogs = Blog.objects.all()
        paginator = self.pagination_class()
        paginated_blogs = paginator.paginate_queryset(blogs, request)
        serializer = BlogSerializer(paginated_blogs, many=True)
        return paginator.get_paginated_response(serializer.data)


@api_view(['POST'])
def post_like(request, pk):
    post = Blog.objects.get(pk=pk)
    post.likes += 1
    post.save()
    serializer = BlogSerializer(post)
    permission_classes = [permissions.IsAuthenticated, ]
    return Response(serializer.data)