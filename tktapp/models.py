from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
class Movies(models.Model):
    name = models.CharField(max_length=50)
    hero = models.CharField(max_length=30)
    heroine = models.CharField(max_length=30)
    director = models.CharField(max_length=30)
    genre = models.CharField(max_length=150,help_text='Seperate genre with spaces',null=True)
    language = models.CharField(max_length=150,help_text='Seperate language with spaces',null=True)
    release_date = models.DateField(help_text='mm/dd/yyyy')
    runtime = models.CharField(max_length=30)
    def __str__(self) :
        return self.name

class Theatre(models.Model):
    theatrename = models.CharField(max_length=30)
    address = models.CharField(max_length=100)
    movie = models.CharField(max_length=30)     
    def __str__(self) :
        return self.theatrename

class Signup(models.Model):    
    email = models.EmailField()
    mobileno = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    def __str__(self) :
        return self.name

class Booking(models.Model):
    Type = (
        ('11:45 am','11:45 am'),
        ('2:45 pm','2:45 pm'),
        ('6:45 pm','6:45 pm'),
        ('9:45 pm','9:45 pm')
    )
    Rate = (
        ('₹100','₹100'),
        ('₹70','₹70')
    )
    CHOICES = (
        ('₹100', (
            ('A','A'),
            ('B','B'),
            ('C','C'),
            ('D','D'),
        )),
        ('₹70', (
            ('F','F'),
            ('G','G'),
            ('H','H'),
        ))
    )
    date = models.DateField(help_text='dd/mm/yyyy')
    showtime = models.CharField(max_length=30,choices=Type)
    ticketprice = models.CharField(max_length=30,choices=Rate)
    screen = models.CharField(max_length=30)
    theatre = models.CharField(max_length=30)
    movie = models.CharField(max_length=30)
    mobile = models.CharField(max_length=30) 
    name = models.CharField(max_length=30)
    select_seat = models.CharField(max_length=30,choices=CHOICES)
    def __str__(self) :
        return self.movie