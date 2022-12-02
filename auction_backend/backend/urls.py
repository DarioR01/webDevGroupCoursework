"""Backend URL Configuration
"""

from django.urls import path

from backend.views import register, login

app_name = 'rainfall_record'
urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login, name='login'),
]
