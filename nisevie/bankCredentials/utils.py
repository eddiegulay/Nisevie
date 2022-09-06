# bank credentials controls
from . models import AccountHolder as AH
from random import randint as rand

# generate otp
def generate_otp():
    token = ""
    for i in range(1,5):
        token += str(rand(0,9))
    return token


# customer login
def customer_login(mobile_number):
    user = AH.objects.get(mobile_number = mobile_number)
    if user:
        token = generate_otp()
        print(f"send _OTP_ {token}")
    else:
        print("Failed to process request")


