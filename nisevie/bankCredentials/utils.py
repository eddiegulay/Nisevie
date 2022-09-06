# bank credentials controls
from . models import AccountHolder as AH


# customer login
def customer_login(mobile_number):
    user = AH.objects.get(mobile_number = mobile_number)
    if user:
        if user.name is "Fin An":
            redirect()

    else:
        render(.)


