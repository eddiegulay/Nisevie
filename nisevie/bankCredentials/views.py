from django.shortcuts import render, redirect
from django.http import JsonResponse
# from .utils import send_otp
from .models import BankAuth as acc_holder
from django.contrib.auth import login, logout
from django.contrib.auth.models import User


# Create your views here.
def get_otp(request, mobile_number):
    resp = {'status': 200, 'otp': 2345, 'customer': 5}
    return JsonResponse(resp)


# customer login
def login_view(request):
    if request.POST:
        mobile = request.POST.get('phoner_number')
        user = acc_holder.objects.get(mobile_number=mobile)
        is_valid_customer = User.objects.get(id=user.holder.id, username=user.holder.username)
        if is_valid_customer is not None:
            login(request, is_valid_customer)
            return redirect('/home')

    return render(request, "login.html")

# send_otp(mobile_number=mobile_number) => {'status': 200, 'otp': 2345}


def customer_logout(request):
    logout(request)
    return redirect("/")