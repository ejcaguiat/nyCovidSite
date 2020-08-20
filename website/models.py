from django.db import models

# Create your models here.
class Case(models.Model):
    date = models.CharField(max_length = 100, blank = False)
    positive = models.IntegerField(null=True, blank=True) #Positive Covid cases
    negative = models.IntegerField(null=True, blank=True) #Negative Covid cases
    recovered = models.IntegerField(null=True, blank=True, default=0) #Recovered Covid cases
    total = models.IntegerField(null=True, blank=True) #Total Covid Tests done
    positiveIncrease = models.IntegerField(null=True, blank=True) #Increase of Positive Covid cases per day
    negativeIncrease = models.IntegerField(null=True, blank=True) #Increase of Negative Covid cases per day
    deathIncrease = models.IntegerField(null=True, blank=True) #Increase of Covid deaths per day
    