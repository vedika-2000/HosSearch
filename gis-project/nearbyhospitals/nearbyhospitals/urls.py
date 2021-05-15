"""nearbyhospitals URL Configuration

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
from django.contrib.gis.admin import OSMGeoAdmin
from django.urls import path
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic.base import TemplateView
from hospitals import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('hospitals/', views.Home.as_view()),
    url(r'^hospitals/', views.Home.as_view(template_name='hospitals/index.html'), name='hospitals'),
    url(r'^$', TemplateView.as_view(template_name='homepage/home.html'),
        name='home'),
    url(r'^homepage/', TemplateView.as_view(template_name='homepage/home.html'),
        name='home'),
    # url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_URL, 'show_indexes': True}),
    # path('api-auth/', include('rest_framework.urls'))
]

urlpatterns += staticfiles_urlpatterns()
