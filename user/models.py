from django.db import models
from django.contrib.auth.models import User

#I will add some fields to the ready user model. So onetoone or foreignkey.
#petowner means that who has a pet.
class Petowner(models.Model):
    user = models.OneToOneField(User, null=True, blank=False, verbose_name="User", on_delete=models.CASCADE)
    tel = models.CharField(max_length=13, verbose_name="Phone")
    address = models.CharField(max_length=100, verbose_name="Address")
    class Meta:
        verbose_name_plural = "Additional information for the user"

    def __str__(self):
        return "{} - {} - {}".format(self.user, self.tel, self.address)
