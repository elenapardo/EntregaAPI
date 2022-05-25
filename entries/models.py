from django.db import models

# Create your models here.
class EntryModel(models.Model):
    datetime = models.DateTimeField()
    concept = models.CharField(max_length=30)
    amount = models.FloatField()
    
    