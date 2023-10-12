from django.db import models
from django.contrib.auth.models import User 

# Create your models here.
class Loan(models.Model):
    user = models.ForeignKey(User,on_delete=models.SET_NULL, blank=True, null=True)
    type = models.CharField(max_length=100)
    clientName = models.CharField(max_length=100)
    PAN = models.CharField(max_length=16)
    number = models.IntegerField()
    amount = models.IntegerField()
    email = models.EmailField(blank=True)
    def __str__(self):
        return self.clientName
    
class Insurance(models.Model):
    user = models.ForeignKey(User,on_delete=models.SET_NULL, blank=True, null=True)
    type = models.CharField(max_length=100)
    clientName = models.CharField(max_length=100)
    PAN = models.CharField(max_length=16)
    number = models.IntegerField()
    amount = models.IntegerField()
    email = models.EmailField(blank=True)
    def __str__(self):
        return self.clientName