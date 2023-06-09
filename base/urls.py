# This url file handle all the routing of base app

from django.urls import path
from . import views 

urlpatterns = [
   path("login/" , views.loginForm, name="login"),
   path("logout/", views.logoutUser, name="logout"),
   path("register/", views.registerPage, name="register"),
   path("",views.home, name="home"),
   path("room/<str:pk>/",views.room, name="room"),
   path("create-room/", views.createRoom, name="create-room"),
   path('update-room/<str:pk>/', views.updateRoom, name="update-room"),
   path("delete-room/<str:pk>", views.deleteRoom, name="delete-room"),
   path("delete-message/<str:pk>", views.deleteMessage, name="delete-message"),
   path("profile/<str:pk>/", views.userProfile, name ="user-profile"),
   path("update-user/", views.UpdateUser, name="update-user"),
]

# path('submit-form/',views.submit_boot , name='submit-form'),