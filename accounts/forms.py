from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from posts.models import Post


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'phone_number', 'email') 

  # yoki agar default user bo‘lsa: from django.contrib.auth.models import User

class EditProfileForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'avatar']  # avatar maydoni mavjud bo‘lsa




