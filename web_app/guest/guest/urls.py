"""guest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from sign import views #导入sign应用中的views文件

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index),#添加index/路径配置
    path('zhanzi/', views.zhanzi),#添加zhanzi/路径配置
    path(r'login/', views.login),#添加login/路径配置
    path('login_action/', views.login_action),
    path('event_manage/', views.event_manage),
    path('', views.login),
    path('accounts/login/', views.login),
]
