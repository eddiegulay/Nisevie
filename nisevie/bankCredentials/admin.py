from django.contrib import admin
from .models import(AccountHolder, BankAccount, SavingsDetail, FixedDepositDetail)

class AccountHolderAdmin(admin.ModelAdmin):
    list_display = ("user_first_name", "user_last_name", "mobile_number")

class BankAccountAdmin(admin.ModelAdmin):
    list_disply = ("account_holder", "account_number", "current_balance")

class SavingsDetailAdmin(admin.ModelAdmin):
    list_display = ("initial_amount", "current_amount", "interest_rates", "time_interval", "bank_account")

class FixedDepositDetailAdmin(admin.ModelAdmin):
    list_display = ("initial_amount", "current_amount", "interest_rates", "time_interval", "bank_account")

admin.site.register(AccountHolder, AccountHolderAdmin)
admin.site.register(BankAccount, BankAccountAdmin)
admin.site.register(SavingsDetail, SavingsDetailAdmin)
admin.site.register(FixedDepositDetail, FixedDepositDetailAdmin)
