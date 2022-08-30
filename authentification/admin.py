from django.contrib.auth.admin import UserAdmin as DefaultUserAdmin
from django.contrib import admin

from .models import  User

@admin.register(User)
class UserAdmin(DefaultUserAdmin):
    list_display=('name','username','password')