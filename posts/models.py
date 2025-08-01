from django.conf import settings
from django.db import models
 
class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    followers = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='following', blank=True)

    def follower_count(self):
        return self.followers.count()


class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='posts/')
    caption = models.TextField(blank=True)
    liked_by = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='liked_posts', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def total_likes(self):
        return self.liked_by.count()

    def total_comments(self):
        return self.comments.count()
class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

from django.conf import settings  # BU KERAK

class Message(models.Model):
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='sent_messages')
    receiver = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='received_messages')
    text = models.TextField(blank=True)
    image = models.ImageField(upload_to='messages/', blank=True, null=True)
    video = models.FileField(upload_to='messages/', blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.sender} → {self.receiver} | {self.text[:30]}"