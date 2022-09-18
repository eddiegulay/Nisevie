# bank credentials controls
from random import randint as rand

from .models import BankAuth as acc_holder
from .models import SavingsDetail as sd
from .models import FixedDepositDetail as fxd
from .models import BankAccount as bank_acc

from .sms_push_otp import send_sms

# generate otp
def generate_otp():
    token = ""
    for i in range(1, 5):
        token += str(rand(0, 9))
    return token


# customer login
def send_otp(mobile_number):
    user = acc_holder.objects.get(mobile_number=mobile_number)
    if user:
        token = generate_otp()
        resp = send_sms(token, mobile_number)
        return resp
    else:
        resp = {'status': 404, 'details': 'Customer Not found'}
        print(resp)
        return resp


# create new customer saving details
def new_customer_saving_plan(bank_acc_id, init_amount, rates, time_interval):
    current_amount = init_amount
    account = bank_acc.objects.get(id=bank_acc_id)
    new_saving_plan = sd.objects.create(bank_account=account, time_interval=time_interval, interest_rates=rates,
                                        initial_amount=init_amount)


# create new customer fixed deposit details
def new_customer_fixed_saving_plan(bank_acc_id, init_amount, rates, time_interval):
    current_amount = init_amount
    account = bank_acc.objects.get(id=bank_acc_id)
    new_saving_plan = fxd.objects.create(bank_account=account, time_interval=time_interval, interest_rates=rates,
                                         initial_amount=init_amount)


# move funds from and into account
def deposit_into_account(acc_number: str, amount: float):
    bank_account = bank_acc.objects.get(account_number=acc_number)
    if bank_account is not None:
        bank_account.current_balance = float(bank_account.current_balance) + float(amount)
        bank_account.save()
    else:
        return False


def withdraw_from_account(acc_number: str, amount: float):
    bank_account = bank_acc.objects.get(account_number=acc_number)
    if bank_account is not None:
        if float(bank_account.current_balance) > float(amount):
            bank_account.current_balance = float(bank_account.current_balance) - float(amount)
            bank_account.save()
            return True
    else:
        return False
