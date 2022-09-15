from django.urls import path
from .views import home_view,advisor_view,advisor_record_incomes, advisor_record_expenses, advisor_suggestion_view, delete_stream_expense, edit_stream_expense, plan_create_view, plans_view, add_missing_stream


urlpatterns = [
    path('', home_view, name='home'),
    path('advisor/', advisor_view, name='advisor'),
    path('streams/', advisor_record_incomes, name='income_streams'),
    path('expenses/', advisor_record_expenses, name='expenses_streams'),
    path('suggestions/', advisor_suggestion_view, name='suggestions'),
    path('delete_expense/<int:_id>', delete_stream_expense, name='delete_expense_stream'),
    path('edit_expense/<int:_id>', edit_stream_expense, name='edit_expense_stream'),
    path('new_plan/', plan_create_view, name='new_plan'),
    path('plans/', plans_view, name='plans_list'),
    path('add_income/', add_missing_stream, name='add_income')
]
