from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Brand(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Car(models.Model):
    BODYTYPE = (
        ('S', 'Sedan'),
        ('3DH', '3-door Hatchback'),
        ('5DH', '5-door Hatchback'),
        ('C', 'Coupe'),
        ('CV', 'Convertible'),
        ('SUV', 'SUV'),
        ('1CP', 'Single Cabin Pick-Up Truck'),
        ('2CP', 'Double Cabin Pick-Up Truck'),
        ('O', 'Other'),
    )
    FUELTYPES = (
                ('NOP','Normal Octane Petrol'),
                ('HOP','High Octane Petrol'),
                ('D','Diesel'),('E','Electric'),
                ('O','Other'),
    )
    owner = models.ForeignKey(User)
    body_type = models.CharField(max_length=10,choices=BODYTYPE)
    brand = models.ForeignKey(Brand, related_name='Car')
    model_name = models.CharField(max_length=200)
    model_year = models.IntegerField()
    engine_type = models.CharField(max_length=300)
    engine_capacity_in_cc = models.IntegerField()
    fuel_type = models.CharField(max_length=20, choices=FUELTYPES)
    drive_type = models.CharField(max_length=100)
    transmission = models.CharField(max_length=100)
    seating_capacity = models.IntegerField()
    mileage_in_kilometres = models.IntegerField()
    color = models.CharField(max_length=100)
    price_in_usd = models.DecimalField(max_digits=12, decimal_places=2)
    description = models.TextField(max_length=1000)
    location = models.CharField(max_length=200)
    is_available = models.BooleanField(default=True)
    is_modified = models.BooleanField(default=False)