from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Post,Comment,Message
from .forms import AddPostForm,CustomUser
from django.contrib.auth import get_user_model
User = get_user_model()
from django.db.models import Q


from posts.models import Post
def profile_view(request, username):
    user = get_object_or_404(User, username=username)
    posts = Post.objects.filter(user=request.user).order_by('-created_at')
    context = {
        'profile_user': user,
        'posts': posts,
    }
    return render(request, 'profile.html', context)

@login_required
def messages_list_view(request):
    users = User.objects.exclude(id=request.user.id)
    return render(request, 'messages/message_list.html', {'users': users})
def home_view(request):
    posts = Post.objects.all().order_by('-created_at')
    users = CustomUser.objects.filter(is_staff=False)
    context = {
        'posts': posts,
        'users': users,
    }
    return render(request, 'home.html', context)


@login_required
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'post_detail.html', {'post': post})

@login_required
def add_post(request):
    if request.method == 'POST':
        form = AddPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('home')
    else:
        form = AddPostForm()
    return render(request, 'add_post.html', {'form': form})
@login_required
def like_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    user = request.user
    if user in post.liked_by.all():
        post.liked_by.remove(user)
    else:
        post.liked_by.add(user)
    return redirect('home')

@login_required
def add_comment(request, post_id):
    if request.method == "POST":
        post = get_object_or_404(Post, pk=post_id)
        content = request.POST.get('content')

        if content:
            Comment.objects.create(
                user=request.user,
                post=post,
                content=content
            )
        return redirect('home')  # Yoki kerakli sahifa nomi
    else:
        return redirect('home')
    


@login_required
def messages_list_view(request):
    users = User.objects.exclude(id=request.user.id)
    return render(request, 'messages_list.html', {'users': users})

from posts.forms import MessageForm

@login_required
def chat_view(request, user_id):
    receiver = get_object_or_404(CustomUser, id=user_id)
    messages = Message.objects.filter(
        Q(sender=request.user, receiver=receiver) |
        Q(sender=receiver, receiver=request.user)
    ).order_by('timestamp')

    if request.method == 'POST':
        form = MessageForm(request.POST, request.FILES)
        if form.is_valid():
            text = form.cleaned_data.get('text')
            image = form.cleaned_data.get('image')
            video = form.cleaned_data.get('video')

            if text or image or video:
                message = form.save(commit=False)
                message.sender = request.user
                message.receiver = receiver
                message.save()
                return redirect('chat', user_id=receiver.id)
    else:
        form = MessageForm()

    return render(request, 'chat.html', {
        'receiver': receiver,
        'messages': messages,
        'form': form
    })
    
