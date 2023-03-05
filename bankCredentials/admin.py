from django.contrib import admin
from .models import(BankAuth, BankAccount, BankService, ServiceBenefit, ServiceRequirements)

class AuthAdmin(admin.ModelAdmin):
    list_display = ("id", "mobile_number")

class BankAccountAdmin(admin.ModelAdmin):
    list_display = ("account_holder", "account_number", "current_balance")

admin.site.register(BankAuth, AuthAdmin)
admin.site.register(BankAccount, BankAccountAdmin)
admin.site.register(BankService)
admin.site.register(ServiceBenefit)
admin.site.register(ServiceRequirements)
