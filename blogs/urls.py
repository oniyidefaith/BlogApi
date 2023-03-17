from django.urls import path, include
from .views import *

urlpatterns = [
    path('create/', PostCreateView.as_view(), name='post_create'),
    path('posts/', PostListView.as_view(), name='post_list'),
    path('<int:pk>/like/', post_like, name='post_like'),
    path('list/', BlogListAPIView.as_view(), name='blog_list'),
]
