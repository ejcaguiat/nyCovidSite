from django.db import models

# Create your models here.
class Case(models.Model):
    date = models.CharField(max_length = 100, blank = False)
    positive = models.IntegerField() #Positive Covid cases
    negative = models.IntegerField() #Negative Covid cases
    recovered = models.IntegerField() #Recovered Covid cases
    total = models.IntegerField() #Total Covid Tests done
    positiveIncrease = models.IntegerField() #Increase of Positive Covid cases per day
    negativeIncrease = models.IntegerField() #Increase of Negative Covid cases per day
    deathIncrease = models.IntegerField() #Increase of Covid deaths per day
