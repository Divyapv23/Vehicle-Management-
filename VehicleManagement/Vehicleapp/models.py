from django.db import models


# Create your models here.


class Vehicle(models.Model):
    VEHICLE_TYPES = (
        ('Two', 'Two Wheeler'),
        ('Three', 'Three Wheeler'),
        ('Four', 'Four Wheeler')
    )

    number = models.CharField(max_length=20, unique=True)
    v_type = models.CharField(max_length=10, choices=VEHICLE_TYPES)
    model = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.number


class adminlogin(models.Model):
    Name = models.CharField(max_length=100, null=True, blank=True)
    Mail = models.EmailField(max_length=100, null=True, blank=True)
    Password = models.CharField(max_length=100, null=True, blank=True)