from django.contrib import admin
from .models import Petowner,Meeting
# Register your models here.
@admin.register(Petowner)
class PetownerAdmin(admin.ModelAdmin):
    list_display = ["user", "tel", "address"]
    list_display_links = ["user", "tel", "address"]
    search_fields = ["user"]

@admin.register(Meeting)
class MeetingAdmin(admin.ModelAdmin):
    list_display = ["user", "pet", "meeting_hour", "meeting_date"]
