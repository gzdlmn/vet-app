from django.db import models
from django.contrib.auth.models import User
from user.models import Petowner




# Create your models here.
#Bir hayvan modeli oluşturduk. Django bize user modelini hazır verdiği için hazır modeli bu modele bağladık.
#Her hayvanın bir sahibi olacak. Buna da petowner dedik.on_delete ise kullanıcı silinirse ona ait hayvanı da sil demek.
#created_date ile kliniğe katılma tarihini otomatik aldık.
class Pet(models.Model):
    petowner = models.ForeignKey("auth.user", on_delete=models.CASCADE)
    image = models.FileField(null=True, blank=True, verbose_name="Resim")
    #Bilerek null blank = True bıraktık. Resim eklemek zorunde değil. Default bir resim koyacağız eklemezse.
    type = models.CharField(max_length=20, verbose_name="Tür")
    genius = models.CharField(max_length=20, verbose_name="Cins")
    name = models.CharField(max_length=20, verbose_name="İsim")
    age = models.CharField(max_length=4, verbose_name="Yaş")
    explanation = models.TextField(verbose_name="Açıklama")
    created_date = models.DateField(auto_now_add=True, verbose_name="Katılma Tarihi")
