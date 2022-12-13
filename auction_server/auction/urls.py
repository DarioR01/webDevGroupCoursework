"""auction_server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from auction import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('login/', views.user_login, name='login'),
    path('registration/', views.registration, name='registration'),
    path('logout/', views.user_logout, name='logout'),
    path('home/', views.home, name='home page'),
    path('item/<int:item_id>', views.item_page, name='item page'),
    path('item/<int:item_id>/<int:question_id>', views.question_answer, name='question answer'),
    path('editProfile/', views.editProfile, name='edit user profile'),
    path('image/', views.upload_image, name='image upload'),
    path('profile/', views.getProfile, name='get profile'),
    path('addNewitem/', views.newItem, name='add new item'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
