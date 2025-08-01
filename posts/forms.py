from django import forms
from .models import Post
from accounts.models import CustomUser 

class AddPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['image', 'caption']

from django import forms
from .models import Post
from accounts.models import CustomUser  # foydalanuvchi modeli


class PostForm(forms.ModelForm):
    user = forms.ModelChoiceField(
        queryset=CustomUser.objects.all(),
        label="Foydalanuvchi",
        widget=forms.Select(attrs={'class': 'form-select'})
    )

    class Meta:
        model = Post
        fields = ['user', 'image', 'caption']

from posts.models import Message

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['text', 'image', 'video']
        widgets = {
            'text': forms.Textarea(attrs={
                'placeholder': 'Xabar yozing...',
                'rows': 1,
                'class': 'form-control'
            }),
        }