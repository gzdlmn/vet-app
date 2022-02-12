from django.contrib import admin
from .models import Pet
# Register your models here.

#first method for admin panel
@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    list_display = ["petowner", "type", "genius", "name", "age", "created_date"]
    list_display_links = ["petowner", "type", "genius", "name", "age", "created_date"]
    search_fields = ["petowner", "name"]
    list_filter = ["type", "genius"]
    class Meta:
        model = Pet
        verbose_name_plural = "Pet"


