"""
URL configuration for template_form_view project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.views.generic import TemplateView 
from app.views import*
urlpatterns = [
    path('admin/', admin.site.urls),
    path('directhtmlpage/',TemplateView.as_view(template_name='directhtmlpage.html'),name='directhtmlpage'),
    path('templatehtml/',templatehtml.as_view(),name='templatehtml'),
    path('insert_schoolby_tv/',insert_schoolby_tv.as_view(),name='insert_schoolby_tv'),
    path('insert_schoolby_fv/',insert_schoolby_fv.as_view(),name='insert_schoolby_fv'),

]
