from django.shortcuts import render

# Create your views here.
# customer login
def login_view(request):
    return render(request, "login.html")
