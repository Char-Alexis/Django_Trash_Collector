from decimal import Decimal

from django.db import models
from .choices import DayOfTheWeek


# Create your models here.

# TODO: Finish customer model by adding necessary properties to fulfill user stories



class Customer(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=50)
    balance = models.DecimalField(max_digits=9, decimal_places=2, default=Decimal('0.00'))
    weekly_pickup_day = models.CharField(max_length=10, choices=DayOfTheWeek.choices, default=DayOfTheWeek.MONDAY)
    one_time_pickup = models.DateField(blank=True, null=True) 
    suspend_start = models.DateField(null=True)
    suspend_end = models.DateField(null=True)
    # suspend_status = 
    # pick_up_status = 


    user = models.ForeignKey('accounts.User', blank=True, null=True, on_delete=models.CASCADE, related_name='customer')