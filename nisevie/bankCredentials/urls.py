from django.urls import path
from .views import login_view, get_otp, customer_logout


urlpatterns = [
    path('', login_view),
    path('otp/<str:mobile_number>', get_otp),
    path('logout/', customer_logout, name='customer_logout')
]
