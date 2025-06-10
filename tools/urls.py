# filepath: c:\Users\micha\OneDrive\Documents\VS Code\om-django\tools\urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('two_ups/', views.two_ups, name='two_ups'),
    path('racing_matcher/', views.racing_matcher, name='racing_matcher'),
    path('willhillbb/', views.willhillbb, name='willhillbb'),
    path("register/", views.register_user, name="register"),
]