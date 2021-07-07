"""ventaPhones URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include
from django.views.generic import TemplateView
from apps.Smartphone import views

from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView, LogoutView



urlpatterns = [
    path('admin/', admin.site.urls),
    
    
    # ===== 1 =====
    # home path
    path('', views.ok, name='home'),
    path('smartphone/', include('apps.Smartphone.urls')),
    
    # path login/logout
    path('login/', LoginView.as_view(redirect_authenticated_user=True, template_name='Usuario/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='UsuariO/logout.html'), name='logout'),    

]
