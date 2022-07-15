from django.contrib import admin
from .models import User, Profile, Announcement
# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('is_learner','is_instructor', 'is_admin')

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display =('user', 'first_name', 'last_name', 'email')