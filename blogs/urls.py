from django.urls import path, include
from .views import *

urlpatterns = [
    path('create/', PostCreateView.as_view(), name='post_create'),
    path('posts/', PostListView.as_view(), name='post_list'),
    path('posts/<int:pk>/like/', post_like, name='post_like'),

]
