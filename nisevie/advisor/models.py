from unicodedata import category
from django.db import models

# Create your models here.
class StreamCategory(models.Model):
    category_name = models.CharField(max_length=30)
    create_date = models.DateTimeField(auto_now=True)

class Stream(models.Model):
    name = models.CharField(max_length=45)
    category = models.ForeignKey(to=StreamCategory, on_delete=models.CASCADE)
    amount = models.FloatField(default=0)
    frequency = models.IntegerField()
    time_interval = models.IntegerField(verbose_name="time interval in months")
    can_save_amount = models.FloatField(default=0)
    least_expenditure = models.FloatField(default=0)
    time_delay = models.IntegerField(default=0, verbose_name="Time delay for the expenditure to occur in months")