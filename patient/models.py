from django.db import models
from django.core.validators import MinValueValidator 
# Create your models here.



class Appointment(models.Model):
    TIME_CHOICES = (
        ("10am - 11am", "10am -11am"),
        ("11am - 12pm", "11am -12pm"),
        ("12pm - 1pm", "12pm -1pm"),
        ("1pm - 2pm", "1pm -2pm"),
        ("2pm - 3pm", "2pm -3pm"),
        ("3pm - 4pm", "3pm -4pm"),
        ("4pm - 5pm", "4pm -5pm"),
        ("5pm - 6pm", "5pm -6pm")
    )
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField(blank=True, null=True, validators=[MinValueValidator(15)])
    phone_number = models.CharField(max_length=11)
    email_address = models.EmailField()
    date = models.DateField(null=True)
    time =  models.CharField(max_length=225, choices=TIME_CHOICES, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)


    def __str__(self):
        return self.name