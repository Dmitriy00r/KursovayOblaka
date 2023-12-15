from django.urls import path

from . import views
from .views import PostUpdateView, PostDeleteView, PostCreateView, PostDetailView, PostListView, UserPostListView, \
    logout_view

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('user/<str:username>', UserPostListView.as_view(template_name='pages/user_posts.html'), name='user-posts'),
    path('post/<int:pk>/', PostDetailView.as_view(template_name='pages/post_detail.html'), name='post-detail'),
    path('post/new/', PostCreateView.as_view(template_name='pages/post_form.html'), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(template_name='pages/post_form.html'), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(template_name='pages/post_confirm_delete.html'), name='post-delete'),
    path('about/', views.about, name='blog-about'),
    path('logout/', logout_view, name='logout'),
]
