from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

class CustomUser(AbstractUser):
    age = models.IntegerField(null=True, blank=True)
    gender = models.CharField(max_length=10, null=True, blank=True)
    additional_info = models.TextField(blank=True,null=True)

class Receipt(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    patient_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    immuneel_patient_id = models.CharField(max_length=100)
    hospital_patient_id = models.CharField(max_length=100)
    receipt_type = models.CharField(max_length=100)
