from django.urls import path
from .views import home_view,advisor_view,advisor_record_incomes, advisor_record_expenses, advisor_suggestion_view


urlpatterns = [
    path('', home_view, name='home'),
    path('advisor/', advisor_view, name='advisor'),
    path('streams/', advisor_record_incomes, name='income_streams'),
    path('expenses/', advisor_record_expenses, name='expenses_streams'),
    path('suggestions/', advisor_suggestion_view, name='suggestions'),
]
