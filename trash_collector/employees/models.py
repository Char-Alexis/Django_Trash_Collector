from django.db import models

# Create your models here.

# TODO: Create an Employee model with properties required by the user stories

class Employees(models.Model):
    # Attributes
    name = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=50)

    # Relationships
    user = models.ForeignKey('accounts.User', blank=True, null=True, on_delete=models.CASCADE)

