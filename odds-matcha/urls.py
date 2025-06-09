from django.contrib import admin
from django.urls import path, include
from tools.views import landing

urlpatterns = [
    path('', landing, name='landing'),
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('tools/', include('tools.urls')),  # <-- Add this line
]