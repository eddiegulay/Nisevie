from django.urls import path
from .views import control_center_view,send_funds,time_jump_view

urlpatterns = [
    path('new_customer/', control_center_view, name='new-customer'),
    path('send_funds/', send_funds, name='send-funds'),
    path('time_jump/', time_jump_view, name='time-jump')
]
