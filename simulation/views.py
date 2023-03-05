from django.shortcuts import render, redirect
from bankCredentials.utils import deposit_into_account, on_deposit_fund_transfer, tagged_on_deposit_fund_transfer

from django.contrib.auth.models import User
from bankCredentials.models import BankAuth, BankAccount
from advisor.models import Stream
from advisor.utils import add_stream

from random import randint as rand

def account_number_generator():
    token = ""
    for i in range(1, 12):
        token += str(rand(1, 9))
    return token

def control_center_view(request):
    if request.POST:
        name = request.POST['customer_name']
        number = request.POST['customer_mobile']
        names = name.split(' ')
        # create user
        new_customer = User(username= names[0], first_name = names[0], last_name = names[1])
        new_customer.save()
        # create auth
        auth_details = BankAuth(mobile_number=number, holder = new_customer)
        auth_details.save()
        # create bankaccount
        acc_number = account_number_generator()
        bank_account = BankAccount(account_holder = new_customer, account_number=acc_number, pass_code=1234)
        bank_account.save()
        # create stream
        add_stream(_linked_account=bank_account.id, is_expense=False, _name="Main Account Balance", _amount=0, _tag=0, _interval=0, _can_save=0, _least_expenditure=0, _time_delay=0)
        return redirect('/simulate/new_customer')

    return render(request, 'sim/center.html')

def send_funds(request):
    if request.POST:
       account_number = request.POST['receivers']     
       tag = request.POST['senders']     
       amount = request.POST['amount']
       # deposit
       # refill all tagged on deposit saving plans
       deposit_amount = tagged_on_deposit_fund_transfer(account_number, tag, amount)
       deposit_into_account(account_number, deposit_amount)

       return redirect("/simulate/send_funds")

    accounts = BankAccount.objects.all()
    context = {
        'accounts': accounts
    }
    return render(request, 'sim/send_funds.html', context)


def time_jump_view(request):
    pass