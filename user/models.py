from django.db import models
from django.contrib.auth.models import User
from pet.models import Pet

# petowner means that who has a pet.I will add some fields to the ready user model. So onetoone or foreignkey.
class Petowner(models.Model):
    user = models.OneToOneField(User, null=True, blank=False, verbose_name="User", on_delete=models.CASCADE)
    tel = models.CharField(max_length=13, verbose_name="Phone")
    address = models.CharField(max_length=100, verbose_name="Address")
    class Meta:
        verbose_name_plural = "Additional information for the user"

    def __str__(self):
        return "{} - {} - {}".format(self.user, self.tel, self.address)

#new model, make an appoinment. A user can make an appoinment for her/his pet. He/she can choose your pet,hour and day.
class Meeting(models.Model):
    user = models.ForeignKey(User, null=True, blank=False, on_delete=models.CASCADE)
    pet = models.ForeignKey(Pet, null=True,blank=False, on_delete=models.CASCADE)
    CHOICES = (('9', '9'), ('10', '10'), ('11', '11'), ('12', '12'), ('13', '13'), ('14', '14'), ('15', '15'), ('16', '16'), ('17', '17'),('18', '18'), ('19', '19'), ('20','20'))
    meeting_hour = models.CharField(choices=CHOICES, max_length=4, null=True, blank=False)
    meeting_date = models.DateField(auto_now_add=False, null=True, blank=False)
    class Meta:
        verbose_name_plural = "Meeting Time"
        ordering = ["meeting_date", "meeting_hour"]




