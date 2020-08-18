from django.db import models

# Create your models here.
class Cases(models.Model):
    date = models.CharField(max_length = 100, blank = False)