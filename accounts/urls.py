from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('signup/', views.signup_view, name='signup'),
    path('edit-profile/', views.edit_profile, name='edit_profile'),
    path('post/<int:pk>/delete/', views.delete_post_view, name='delete_post'),

]