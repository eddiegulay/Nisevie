from django.db import models
from bankCredentials.models import BankAccount

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

class SavingPlan(models.Model):
    target_account =  models.ForeignKey(to=BankAccount, verbose_name=_("target account"), on_delete=models.CASCADE)
    create_time = models.DateTimeField(auto_now = True)
    time_interval = models.IntegerField(default=0)
    income_stream = models.ForeignKey(to=Stream, on_delete=models.CASCADE)
    initial_amount = models.BigIntegerField(default=0)
    allowed_withdraw_date = models.DateTimeField()
    is_frequency_allowed = models.BooleanField(default=False)
    deposit_frequency = models.IntegerField(default=1)
    frequency_deposit_amount = models.BigIntegerField(default=0)