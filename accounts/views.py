
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import EditProfileForm



def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def edit_profile(request):
    user = request.user
    if request.method == 'POST':
        form = EditProfileForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = EditProfileForm(instance=user)
    return render(request, 'edit_profile.html', {'form': form})


from .forms import CustomUserCreationForm
from django.contrib.auth import login

def signup_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # yoki boshqa sahifaga
    else:
        form = CustomUserCreationForm()
    
    return render(request, 'signup.html', {'form': form})

from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from posts.models import Post

@login_required
def delete_post_view(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if post.user == request.user:
        post.delete()
    return redirect('home')  # yoki asosiy postlar sahifasi


