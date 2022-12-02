"""Backend URL Configuration
"""

from django.urls import path

from backend.views import create_user

app_name = 'rainfall_record'
urlpatterns = [
    path('register/', create_user, name='register'),
]
