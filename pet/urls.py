from django.contrib import admin
from django.urls import path
from . import views
#url leri dinamik yazmak için app_name vermek önemli
app_name = "pet"

urlpatterns = [
    path('pets/', views.all_pets, name='pets'),
    #path('dashboard/', views.dashboard, name='dashboard'),
    path('addpet/', views.add_pet, name='addpet'),
    path('detail/<int:id>', views.detail, name='detail'),
    path('update/<int:id>', views.update, name="update"),
    path('delete/<int:id>', views.delete, name='delete'),
]