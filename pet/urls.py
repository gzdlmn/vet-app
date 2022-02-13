from django.contrib import admin
from django.urls import path
from . import views
#app_name is very important in django. Because we use dynamic url. {% url 'pet:pets' %} instead of /pet/pets. We don't write like that!
app_name = "pet"

urlpatterns = [
    path('pets/', views.all_pets, name='pets'),
    path('addpet/', views.add_pet, name='addpet'),
    path('detail/<int:id>', views.detail, name='detail'),
    path('update/<int:id>', views.update, name="update"),
    path('delete/<int:id>', views.delete, name='delete'),
    path('appointments/', views.meeting, name="appointments"),
    path('delete_meeting/<int:id>', views.delete_meeting, name='delete_meeting'),
]