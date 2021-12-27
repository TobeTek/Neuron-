# admin.py
from django.contrib import admin
from .models import Profile, CustomUser
from django.contrib.auth.admin import UserAdmin

class UserProfileInline(admin.StackedInline):
    model = Profile

class CustomUserAdmin(UserAdmin):
    inlines = [UserProfileInline]

admin.site.register(CustomUser, CustomUserAdmin)