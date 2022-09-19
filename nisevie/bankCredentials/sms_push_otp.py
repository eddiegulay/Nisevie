import os
from twilio.rest import Client
from random import randint as rand


def send_sms(otp: str, number: str):
    # try:
    account_sid = "ACffd7c55f6c817b44dfce790a0814be21"
    auth_token = "86a3bb12514c4d7ba52110e56f367415"
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
        body=f"Your Nisevie OTP is: {otp}",
        from_='+13854427217',
        to=number
    )
    return {'status': 200, 'otp': otp}
    # except:
    #     print("error")
    #     return {'status': 500, 'details': 'Failed to send OTP'}
