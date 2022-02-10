"""vet URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from home.views import homepage
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from user.views import *
from pet.views import *

#home ve pet birer app. homepage tek bir fonksiyon olduğu için ana url e direk bağlandı. pet ise pet/ altında farklı bir sürü sayfaya
#gideceği içi include ile bağlandı
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage, name='homepage'),
    path('pet/', include('pet.urls')),
    path('user/', include('user.urls')),
]

urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT )
