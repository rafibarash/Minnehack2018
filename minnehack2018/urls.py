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
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/', TemplateView.as_view(template_name='concussiontest/pages/about.html'), name='about'),
    path('test/', TemplateView.as_view(template_name='concussiontest/pages/test.html'), name='test'),
	path('visual/', TemplateView.as_view(template_name='concussiontest/pages/visual.html'), name='visual'),
    path('resources/', TemplateView.as_view(template_name='concussiontest/pages/resources.html'), name='resources'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('signup/', include('registration.urls')),
    # Must be last
    path('', TemplateView.as_view(template_name='concussiontest/pages/home.html'), name='home'),
]
