import os
from twilio.rest import Client
from random import randint as rand

def send_sms(otp: str):
    try:
        account_sid = "ACffd7c55f6c817b44dfce790a0814be21"
        auth_token = "74035b4ad2a3ab857150a5cdeafa3334"
        client = Client(account_sid, auth_token)

        message = client.messages \
            .create(
                body=f"Your Nisevie OTP is: {otp}",
                from_='+13854427217',
                to='+255748173751'
            )
    except:
        return None

# generate otp
def generate_otp():
    token = ""
    for i in range(1,5):
        token += str(rand(0,9))
    return token

token =generate_otp()
send_sms(token)
print(f"OTP: {token}")
