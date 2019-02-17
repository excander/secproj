from django.contrib import admin

from .models import User, User_data

admin.site.register(User)
admin.site.register(User_data)