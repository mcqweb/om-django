from django.contrib import admin
from .models import Tool, UserToolPermission

admin.site.register(Tool)
admin.site.register(UserToolPermission)
