from django.db import models

from bankCredentials.models import BankAccount


# Create your models here.
class StreamCategory(models.Model):
    category_name = models.CharField(max_length=30)
    create_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.category_name


class Stream(models.Model):
    name = models.CharField(max_length=45)
    linked_account = models.ForeignKey(to=BankAccount, on_delete=models.CASCADE)
    category = models.ForeignKey(to=StreamCategory, on_delete=models.CASCADE)
    amount = models.FloatField(default=0)
    tag = models.CharField(max_length=50, default='000000000000')
    time_interval = models.IntegerField(verbose_name="time interval in months")
    can_save_amount = models.FloatField(default=0)
    least_expenditure = models.FloatField(default=0)
    time_delay = models.IntegerField(default=0, verbose_name="Time delay for the expenditure to occur in months")

    def __str__(self):
        return self.name
    

class SavingPlan(models.Model):
    plan_name = models.CharField(max_length=100)
    target_account = models.ForeignKey(to=BankAccount, verbose_name="target account", on_delete=models.CASCADE)
    create_time = models.DateField(auto_now=True)
    time_interval = models.IntegerField(default=0)
    income_stream = models.ForeignKey(to=Stream, on_delete=models.CASCADE)
    current_amount = models.BigIntegerField(default=0)
    allowed_withdraw_date = models.DateField()
    deposit_frequency = models.IntegerField(default=1)
    frequency_deposit_amount = models.BigIntegerField(default=0)
    is_active = models.BooleanField(default=False)
    is_fixed = models.BooleanField(default=False)

    def __str__(self):
        return f"Plan {self.plan_name}"