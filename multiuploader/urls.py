"""multiuploader URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import re_path, path

from multiuploader import views

urlpatterns = [
    path('uploadhome',views.uploadHome),
    re_path(r'^multiuploader_delete_multiple/$', views.multiuploader_delete_multiple,
        name='multiuploader_delete_multiple'),
    re_path(r'^multiuploader_delete/(?P<pk>\w+)/$', views.multiuploader_delete,
        name='multiuploader_delete'),
    re_path(r'^multiuploader/$', views.multiuploader, name='multiuploader'),
    re_path(r'^multiuploader_noajax/$', views.multiuploader, kwargs={"noajax": True},
        name='multiploader_noajax'),
    re_path(r'^multiuploader_file/(?P<pk>\w*)/$', views.multi_show_uploaded,
        name='multiuploader_file_link'),
    re_path(r'^multiuploader_get_files_noajax/$', views.multi_get_files, kwargs={"noajax": True},
        name='multiuploader_get_files_noajax'),
    re_path(r'^multiuploader_get_files/(?P<fieldname>\w*)/$', views.multi_get_files,
        name='multi_get_files'),
]