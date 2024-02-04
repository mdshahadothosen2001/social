from django.urls import path
from .views import PostList, CreatePostView

urlpatterns = [
    path('posts/', PostList.as_view(), name='post-list'),
    path("create/", CreatePostView.as_view()),
]