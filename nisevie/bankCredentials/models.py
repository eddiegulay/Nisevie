from django.db import models
from django.contrib.auth.models import User as AccountHolder

# Create your models here.
class BankAuth(models.Model):
    mobile_number = models.CharField(max_length=20, unique=True, null=True)
    holder = models.ForeignKey(AccountHolder, on_delete=models.CASCADE)

class BankAccount(models.Model):
    account_holder = models.ForeignKey(to=AccountHolder, on_delete=models.CASCADE)
    account_number = models.BigIntegerField(verbose_name="account number")
    pass_code = models.SmallIntegerField(verbose_name="Pass code")
    current_balance = models.FloatField(default=0)

    def __str__(self) -> str:
        return f"{self.account_holder.first_name} {self.account_holder.last_name} ({self.account_number})"


class SavingAccount(models.Model):
    initial_amount = models.FloatField(default=0)
    current_amount = models.FloatField(default=0)
    interest_rates = models.FloatField(default=1.2)
    time_interval = models.IntegerField(verbose_name="Saving time frame")
    bank_account = models.ForeignKey(to=BankAccount, on_delete=models.CASCADE)
    create_time = models.DateTimeField(auto_now=True)


class SavingsDetail(SavingAccount):
    pass


class FixedDepositDetail(SavingAccount):
    pass
