from django.db import models

# Create your models here.
class AccountHolder(models.Model):
    user_first_name = models.CharField(max_length=45)
    user_last_name = models.CharField(max_length=45)
    mobile_number = models.CharField(max_length=14, verbose_name="Phone number")

    def __str__(self) -> str:
        return f"{self.user_first_name} {self.user_last_name}"

class BankAccount(models.Model):
    account_holder = models.ForeignKey(to=AccountHolder, on_delete=models.CASCADE)
    account_number = models.BigIntegerField(verbose_name="account number")
    pass_code = models.SmallIntegerField(verbose_name="Pass code")
    current_balance = models.FloatField(default=0)

    def __str__(self) -> str:
        return f"{self.account_number}@{self.account_holder.mobile_number}"

class SavingAccount(models.Model):
    initial_amount = models.FloatField(default=0)
    current_amount = models.FloatField(default=0)
    interest_rates = models.FloatField(default=1.2)
    time_interval = models.IntegerField(verbose_name="Saving time frame")
    bank_account = models.ForeignKey(to=BankAccount, on_delete=models.CASCADE)

class SavingsDetail(SavingAccount):
    pass

class FixedDepositDetail(SavingAccount):
    pass
