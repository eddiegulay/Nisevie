from django.urls import path
from .views import home_view,advisor_view


urlpatterns = [
    path('', home_view, name='home'),
    path('advisor/', advisor_view, name='advisor')
]
