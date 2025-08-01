from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('like/<int:pk>/', views.like_post, name='like_post'),
    path('add-post/', views.add_post, name='add_post'),
    path('post/<int:post_id>/add_comment/', views.add_comment, name='add_comment'),
    path('messages/', views.messages_list_view, name='messages'),
    path('messages/<int:user_id>/', views.chat_view, name='chat'),
path('profile/<str:username>/', views.profile_view, name='profile'),


]
