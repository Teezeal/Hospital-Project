from django.contrib import admin
from.models import Appointment
# Register your models here.
@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ["name", "phone_number", "email_address", "date_created"]
    list_filter = ["time", "date_created", "date"]
    search_fields = ["name", "phone_number", "email_address"]