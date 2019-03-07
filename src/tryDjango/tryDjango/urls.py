"""tryDjango URL Configuration

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
from page.views import home_view, contact_view, about_view


urlpatterns = [
    path('blog/', include('blog.urls', namespace="blog")),
    path('course/', include('course.urls', namespace="course")),


    
    path('product/', include('products.urls')),
    path('person/', include('personinfo.urls')),
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),
    path('contact/', contact_view, name='contact'),
    path('about/<int:p_id>', about_view, name='product-detail'), # illustration purpose
    path('about', about_view, name='about'),
    
]
