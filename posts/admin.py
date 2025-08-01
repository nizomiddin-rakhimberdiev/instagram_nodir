from django.contrib import admin

# Register your models here.
from posts.models import Post, Comment
from django.contrib import admin
from .models import Post, Profile, Comment


admin.site.register(Profile)


class PostAdmin(admin.ModelAdmin):

    list_display = ('user', 'caption', 'created_at')
    search_fields = ('caption',)
    list_filter = ('created_at',)
    


class CommentAdmin(admin.ModelAdmin):

    list_display = ('post', 'user', 'created_at')
    search_fields = ('content',)
    list_filter = ('created_at',)
class CategoryAdmin(admin.ModelAdmin):

    list_display = ('name',)
    search_fields = ('name',)
    list_filter = ('name',)
admin.site.register(Post)
admin.site.register(Comment)


