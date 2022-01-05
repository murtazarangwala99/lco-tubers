from django.db import models
from datetime import datetime
# Create your models here.
class Contactus(models.Model):
    
    full_name = models.CharField(max_length=100)
    phone_number = models.IntegerField()
    email = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    message = models.CharField(max_length=255)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name