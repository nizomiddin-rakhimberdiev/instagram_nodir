
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ('Extra info', {'fields': ('avatar',)}),
    )

    list_display = ('username', 'email', 'avatar', 'is_staff')

admin.site.register(CustomUser, CustomUserAdmin)


