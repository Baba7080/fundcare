from django.db import models
from django.contrib.auth.models import User 
import datetime
from datetime import date
from django.utils import timezone
# Create your models here.


WORKTYPE_CHOICE = (
    ('Student','Student'),
    ('Driver','Driver'),
    ('Employee','Employee'),
    ('Shop owner','Shop owner'),
    ('Delivery boy','Delivery boy'),
    ('Other','Other')
)

GENDER_CHOICE = (
  ('Male','Male'),
    ('Female','Female'),
)

ADDRESS_CHOICE = (
    ('Home with Family','Home with Family'),
    ('Rented with Family','Rented with Family'),
    ('Rented with Friends','Rented with Friends'),
    ('Hostel/PG','Hostel/PG')
)

class frenchise_register_model(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    frenchise_name = models.CharField(max_length=30)
    
    DOB = models.DateField(max_length=8,null=True)
    gender = models.CharField(max_length=20, choices=GENDER_CHOICE)
    # Age = models.IntegerField(null=True) 
    city =models.CharField(max_length=20,null=True)
    Pin_code = models.PositiveIntegerField()

    Work_Type = models.CharField(max_length=20, choices=WORKTYPE_CHOICE)
    Address_Type = models.CharField(max_length=50, choices=ADDRESS_CHOICE)



#Employee Registration

# class employee_registration_model(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     email = models.EmailField(null=False)
#     password = models.CharField(max_length=50)



class frenchise_employee_register_model(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    employee_id = models.IntegerField(default=123456)
    email = models.EmailField(null=False, blank=False, default= 'employee@gmail.com')
    username = models.CharField(max_length=15,null=False, blank=False, default='Username')
    password = models.CharField(max_length=50)
    # Role = models.CharField(max_length=120,default="not specified")
   
    
class ProfileFrenchise(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    frenchise_name = models.CharField(max_length=30)
    Code = models.CharField(max_length=100)
    email = models.EmailField(blank=True)
    DOB = models.DateField(max_length=8,null=True)
    gender = models.CharField(max_length=20)
    # Age = models.IntegerField(null=True)
    city =models.CharField(max_length=20,null=True)
    state = models.CharField(max_length=100)
    number = models.IntegerField(max_length=10)
    Education = models.CharField(max_length=100)
    Occupation = models.CharField(max_length=100)
    Address_Type = models.CharField(max_length=50)
    Role = models.CharField(max_length=120,default="not specified")
    def __str__(self):
        return f"{self.number}"