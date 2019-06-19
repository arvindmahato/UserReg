from django.urls import path
from .views import (
    blog,
    PostDetailView,
    PostCreatelView,
    PostUpdatelView,
    PostDeletelView,
    UserPostListView,
    about,
)

urlpatterns = [
    path('', blog.as_view(), name='blog'),
    path('post/<str:username>/', UserPostListView.as_view(), name='user-posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreatelView.as_view(), name='post-new'),
    path('post/<int:pk>/update/', PostUpdatelView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeletelView.as_view(), name='post-delete'),
    path('about/', about, name='about'),
]