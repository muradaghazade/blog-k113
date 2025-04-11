from django.db import models

class Car(models.Model):
    marka = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField()
    odometer = models.IntegerField()
    engine = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    text = models.TextField()
    image = models.ImageField(upload_to='images/', null=True, blank=True)

class Phone(models.Model):
    name = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    ram = models.IntegerField()
    storage = models.IntegerField()
    price = models.IntegerField()
    image = models.ImageField(upload_to='images/')