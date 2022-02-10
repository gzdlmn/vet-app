from django.db import models
from django.contrib.auth.models import User
from user.models import Petowner


# Create your models here.
#created pet model. I used user model which is in django.
#there is a petowner for each pet. if petowner is deleted, pet will delete. (on_delete means that)
#created_date automatically create.
class Pet(models.Model):
    petowner = models.ForeignKey("auth.user", on_delete=models.CASCADE)
    image = models.FileField(null=True, blank=True, verbose_name="Image")
    #Bilerek null blank = True bıraktık. Resim eklemek zorunde değil. Default bir resim koyacağız eklemezse.
    type = models.CharField(max_length=20, verbose_name="Type")
    genius = models.CharField(max_length=20, verbose_name="Genius")
    name = models.CharField(max_length=20, verbose_name="Name")
    age = models.CharField(max_length=4, verbose_name="Age")
    explanation = models.TextField(verbose_name="Explanation")
    created_date = models.DateField(auto_now_add=True, verbose_name="Created Date")
