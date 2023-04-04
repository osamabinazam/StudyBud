
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include('base.urls')),     # referencing the urls.py script of base appn
]
