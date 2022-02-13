from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

app_name='user'
urlpatterns=[
    path('register/', views.register, name="register"),
    path('login/', views.loginUser, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('petowner/<username>', views.petowner, name="petowner"), #special page for user /petowner/username/blablaba..
    path('appointments/', views.meeting, name="appointments")
]