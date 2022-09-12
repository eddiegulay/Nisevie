from django.contrib import admin
from .models import(BankAuth, BankAccount, SavingsDetail, FixedDepositDetail)

class AuthAdmin(admin.ModelAdmin):
    list_display = ("id", "mobile_number")

class BankAccountAdmin(admin.ModelAdmin):
    list_display = ("account_holder", "account_number", "current_balance")

class SavingsDetailAdmin(admin.ModelAdmin):
    list_display = ("initial_amount", "current_amount", "interest_rates", "time_interval", "bank_account")

class FixedDepositDetailAdmin(admin.ModelAdmin):
    list_display = ("initial_amount", "current_amount", "interest_rates", "time_interval", "bank_account")

admin.site.register(BankAuth, AuthAdmin)
admin.site.register(BankAccount, BankAccountAdmin)
admin.site.register(SavingsDetail, SavingsDetailAdmin)
admin.site.register(FixedDepositDetail, FixedDepositDetailAdmin)
