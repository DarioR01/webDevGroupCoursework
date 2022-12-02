"""Backend URL Configuration
"""

from django.urls import path

from backend.views import register

app_name = 'rainfall_record'
urlpatterns = [
    path('register/', register, name='register'),
]
