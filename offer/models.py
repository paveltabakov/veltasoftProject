from django.db import models
from django.utils import timezone

# Create your models here.
class Offer(models.Model):
    customerName = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    subject = models.CharField(max_length=200)
    message = models.CharField(max_length=300)
    created_date = models.DateTimeField(default=timezone.now)
    
    
    def __str__(self): #private method  toString()
        return (self.email, self.customerName, self.message, self.subject)