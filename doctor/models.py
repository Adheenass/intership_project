from django.db import models

# Create your models here.


class Doctor(models.Model):

    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
      ]

    d_name = models.CharField(max_length=100)
    department_name = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)
    available_date = models.DateField()
    time_slot = models.DurationField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)

