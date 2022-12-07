"""Backend URL Configuration
"""

from django.urls import path

from backend.views import register, login, logout, name

app_name = 'rainfall_record'
urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('item/<int:item_id>/', name, name='name'),
]
