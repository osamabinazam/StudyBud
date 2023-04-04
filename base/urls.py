# This url file handle all the routing of base app

from django.urls import path
from . import views 

urlpatterns = [
   path("",views.home, name="home"),
   path("room/",views.room, name="room"),
]
