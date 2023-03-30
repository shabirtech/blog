from django.urls import path
from .views import home,create_post, BlogPostList, BlogPostDetail

urlpatterns = [
    path("", home, name="home"),
    path("create_post/", create_post, name="create_post"),
    path('api/blog-posts/', BlogPostList.as_view()),
    path('api/blog-posts/<int:pk>/', BlogPostDetail.as_view()),
]