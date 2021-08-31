from django.db import models

class DayOfTheWeek(models.TextChoices):
    MONDAY = 'Monday'
    TUESDAY = 'Tuesday'