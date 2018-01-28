"""minnehack2018 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path
import django.contrib.auth.views as auth_views
from . import views

urlpatterns = [
    # url(r'^login/$', views.user_login, name='login'),

    path('register/', views.register, name='register'),
    path('profile/', views.dashboard, name='dashboard'), # Dashboard
    path('edit/', views.edit, name='edit'),

    # login / logout urls
    path('login/', auth_views.LoginView.as_view(template_name='account/login.html'), name='login'),
    path('logout/', auth_views.logout, name='logout'),
    path('logout-then-login/', auth_views.logout_then_login, name='logout_then_login'),

    # change password urls
    path('password-change/', auth_views.password_change, name='password_change'),
    path('password-change/done/', auth_views.password_change_done, name='password_change_done'),

    # restore password urls
    path('password-reset/', auth_views.password_reset, name='password_reset'),
    path('password-reset/done/', auth_views.password_reset_done, name='password_reset_done'),
    path('password-reset/confirm/(?P<uidb64>[-\w]+)/(?P<token>[-\w]+)/', auth_views.password_reset_confirm,
         name='password_reset_confirm'),
    path('password-reset/complete/', auth_views.password_reset_complete, name='password_reset_complete'),


]
