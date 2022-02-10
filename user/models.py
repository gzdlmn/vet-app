from django.db import models
from django.contrib.auth.models import User

# Create your models here. user modeline ek alanlar eklemek için onetonone ile ilşkilendiriyorum. tel address hazır user modelinde yok

class Petowner(models.Model):
    user = models.OneToOneField(User, null=True, blank=False, verbose_name="Kullanıcı", on_delete=models.CASCADE)
    tel = models.CharField(max_length=13, verbose_name="Tel")
    address = models.CharField(max_length=100, verbose_name="Adres")
    class Meta:
        verbose_name_plural = "Kullanıcılar Ek Bilgiler"

    def __str__(self):
        return "{} - {} - {}".format(self.user, self.tel, self.address)
