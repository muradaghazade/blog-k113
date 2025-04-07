from django.db import models

class Car(models.Model):
    marka = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField()
    odometer = models.IntegerField()
    engine = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    text = models.TextField()