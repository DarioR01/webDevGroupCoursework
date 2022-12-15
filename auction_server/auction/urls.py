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
from django.urls import path, re_path
from auction import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('api/login/', views.user_login, name='login'),
    path('api/registration/', views.registration, name='registration'),
    path('api/logout/', views.user_logout, name='logout'),
    path('api/home/', views.home, name='home page'),
    re_path(r'^api/home/(?P<filter>\w+)/$', views.home, name='filter'),
    path('api/item/<int:item_id>', views.item_page, name='item page'),
    path('api/item/<int:item_id>/<int:question_id>', views.question_answer, name='question answer'),
    path('api/profile/', views.profile_page, name='profile'),
    path('api/profile/<int:item_id>', views.upload_item_image, name='profile profile'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
