from django.db import models

# Create your models here.
class Case(models.Model):
    date = models.CharField(max_length = 100, blank = False)
    positive = models.IntegerField(default=0) #Positive Covid cases
    negative = models.IntegerField(default=0) #Negative Covid cases
    recovered = models.IntegerField(default=0) #Recovered Covid cases
    total = models.IntegerField(default=0) #Total Covid Tests done
    positiveIncrease = models.IntegerField(default=0) #Increase of Positive Covid cases per day
    negativeIncrease = models.IntegerField(default=0) #Increase of Negative Covid cases per day
    deathIncrease = models.IntegerField(default=0) #Increase of Covid deaths per day
    