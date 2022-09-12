from django.urls import path
from .views import login_view, get_otp


urlpatterns = [
    path('', login_view),
    path('otp/<str:mobile_number>', get_otp)
]
