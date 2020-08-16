from django.db import models
from django.contrib.auth.models import User

# Create your models here.
location_choices = [
    ('Choice1','CHOICE1'),
    ('Choice2','CHOICE2'),
    ('Choice3','CHOICE3')
]

class Profile(models.Model):
    user_types = [
        ('ADMIN','Admin'),
        ('USER','User'),
        ('VIEWER','Viewer'),
        ('UNASSIGNED','Unassigned')
    ]
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    name = models.CharField(max_length = 50)
    user_type = models.CharField(max_length = 50,choices = user_types,default = 'Unassigned')

class Form1model(models.Model):
    name = models.CharField(max_length = 50)
    location = models.CharField(max_length = 50,choices = location_choices)
    date = models.DateTimeField(auto_now=True)
    vehicle_number = models.CharField(max_length=50)
    Quantity = models.IntegerField()
    num_trips = models.IntegerField()
    type_waste = models.CharField(max_length = 50)
    image = models.ImageField(blank = True)
    comments = models.CharField(max_length=50,blank = True)
