from django.shortcuts import render, redirect

from django.contrib.auth.models import User as AccountHolder
from advisor.models import SavingPlan, Stream, StreamCategory
from bankCredentials.models import BankAccount
from bankCredentials.utils import deposit_into_account, withdraw_from_account   
from .utils import add_stream, calculate_stream_total, calculate_plan_total


def login_auth(_id):
    try:
        customer = AccountHolder.objects.get(id=_id)
        return False
    except:
        return redirect('/')


# 🌟
def home_view(request):
    holder_id = request.user.id
    customer = AccountHolder.objects.get(id=holder_id)
    bank_account = BankAccount.objects.get(account_holder=customer)

    # saving plans 
    saving_plans = SavingPlan.objects.filter(target_account=bank_account)
    context = {
        'bank_account':bank_account
    }
    return render(request, 'home.html', context)


# plan advisor landing page
def advisor_view(request):
    return render(request, 'advisor/advisor.html')


# plan advisor record income streams
def advisor_record_incomes(request):
    if request.POST:
        stream_name = request.POST['stream_name']
        stream_amount = request.POST['stream_amount']
        time_interval = request.POST['time_interval']
        stream_frequency = request.POST['stream_frequency']
        add_stream(request.user.id, False, stream_name, stream_amount, stream_frequency, time_interval, 0, 0, 0)
        return redirect('/home/streams/')

    # active income streams
    holder = AccountHolder.objects.get(id=request.user.id)  # account holder
    account = BankAccount.objects.get(account_holder=holder)  # account linked to income stream
    stream_category = StreamCategory.objects.get(
        category_name="Income")  # category classification separating Expenses from Incomes

    income_streams = Stream.objects.filter(category=stream_category, linked_account=account)

    context = {
        'income_streams': income_streams
    }
    return render(request, 'advisor/income_streams.html', context)


def advisor_record_expenses(request):
    if request.POST:
        stream_name = request.POST['stream_name']
        stream_amount = request.POST['stream_amount']
        time_interval = request.POST['time_interval']
        stream_frequency = request.POST['stream_frequency']
        can_save_amount = request.POST['can_save_amount']
        least_expenditure = request.POST['least_expenditure']

        add_stream(request.user.id, True, stream_name, stream_amount, stream_frequency, time_interval, can_save_amount,
                   least_expenditure, 0)
        return redirect('/home/expenses/')

    # active expense streams
    holder = AccountHolder.objects.get(id=request.user.id)  # account holder
    account = BankAccount.objects.get(account_holder=holder)  # account linked to income stream
    stream_category = StreamCategory.objects.get(
        category_name="Expense")  # category classification separating Expenses from Incomes

    expenses = Stream.objects.filter(category=stream_category, linked_account=account)

    context = {
        'expenses': expenses
    }
    return render(request, 'advisor/expense_streams.html', context)


def delete_stream_expense(request, _id):
    stream = Stream.objects.get(id=_id)
    stream.delete()

    return redirect("/home/expenses/")


def edit_stream_expense(request, _id):
    stream = Stream.objects.get(id=_id)
    if request.POST:
        stream.name = request.POST['stream_name']
        stream.amount = request.POST['stream_amount']
        stream.time_interval = request.POST['time_interval']
        stream.frequency = request.POST['stream_frequency']
        stream.can_save_amount = request.POST['can_save_amount']
        stream.least_expenditure = request.POST['least_expenditure']

        stream.save()
        return redirect('/home/expenses/')

    context = {
        'expense': stream
    }
    return render(request, 'advisor/edit_expense.html', context)


def advisor_suggestion_view(request):
    holder = AccountHolder.objects.get(id=request.user.id)  # account holder
    account = BankAccount.objects.get(account_holder=holder)  # account linked to income stream
    total_income = 0

    # active expense streams
    expense_category = StreamCategory.objects.get(category_name="Expense")
    expense_list = Stream.objects.filter(category=expense_category, linked_account=account)
    expenses = Stream.objects.filter(category=expense_category, linked_account=account).values()
    total_expenses = calculate_stream_total(list(expenses))
    # active income streams
    stream_category = StreamCategory.objects.get(category_name="Income")
    income_streams = Stream.objects.filter(category=stream_category, linked_account=account).values()
    income_list = Stream.objects.filter(category=stream_category, linked_account=account)
    total_income = calculate_stream_total(list(income_streams))

    context = {
        'total_income': total_income,
        'total_expense': total_expenses,
        'expense_list': expense_list,
        'income_list': income_list
    }

    return render(request, 'advisor/suggestions.html', context)


# 🐛
def plan_create_view(request):
    holder_id = request.user.id
    customer = AccountHolder.objects.get(id=holder_id)
    bank_account = BankAccount.objects.get(account_holder=customer)

    stream_category = StreamCategory.objects.get(category_name="Income")
    income_list = Stream.objects.filter(category=stream_category, linked_account=bank_account)

    # saving plans 
    saving_plans = SavingPlan.objects.filter(target_account=bank_account)

    if request.POST:
        income_stream = request.POST['income_name']
        initial_amount = request.POST['initial_amount']
        time_interval = request.POST['time_interval']
        start_date = request.POST['start_date']
        end_date = request.POST['end_date']
        plan_name = request.POST['plan_name']
        
        income = Stream.objects.get(id= income_stream)
        # reduce 
        withdraw_from_account(bank_account.account_number, initial_amount)

        new_plan = SavingPlan(plan_name=plan_name, target_account = bank_account, create_time=start_date, time_interval=time_interval, income_stream=income, initial_amount=initial_amount, current_amount=initial_amount, frequency_deposit_amount=initial_amount, is_current=True, allowed_withdraw_date=end_date)

        income = Stream.objects.get(id=income_stream)

        new_plan = SavingPlan(target_account=bank_account, create_time=start_date, time_interval=time_interval,
                              income_stream=income, initial_amount=initial_amount, current_amount=initial_amount,
                              frequency_deposit_amount=initial_amount, is_current=True, allowed_withdraw_date=end_date)
        new_plan.save()
        return redirect('.')

    return render(request, 'advisor/create_plan.html', {'plans': saving_plans, 'streams': income_list})


def plans_view(request):
    holder_id = request.user.id
    customer = AccountHolder.objects.get(id=holder_id)
    bank_account = BankAccount.objects.get(account_holder=customer)

    # saving plans 
    saving_plans = SavingPlan.objects.filter(target_account=bank_account)
    active_plans = SavingPlan.objects.filter(target_account=bank_account, is_current=True)
    balance = calculate_plan_total(active_plans)

    context = {
        'plans': saving_plans,
        'plans_count': len(active_plans),
        'total_amount': balance,
        'bank_account': bank_account
    }
    return render(request, 'advisor/inactive_plan.html', context)


def add_missing_stream(request):
    if request.POST:
        stream_name = request.POST['stream_name']
        stream_amount = request.POST['stream_amount']
        time_interval = request.POST['time_interval']
        stream_frequency = request.POST['stream_frequency']
        add_stream(request.user.id, False, stream_name, stream_amount, stream_frequency, time_interval, 0, 0, 0)
        return redirect('/home/new_plan/')

    # active income streams
    holder = AccountHolder.objects.get(id=request.user.id)  # account holder
    account = BankAccount.objects.get(account_holder=holder)  # account linked to income stream
    stream_category = StreamCategory.objects.get(
        category_name="Income")  # category classification separating Expenses from Incomes

    income_streams = Stream.objects.filter(category=stream_category, linked_account=account)

    context = {
        'income_streams': income_streams
    }
    return render(request, 'advisor/income_streams.html', context)


def deactivate_plan(request, plan_id):
    holder_id = request.user.id
    customer = AccountHolder.objects.get(id=holder_id)
    bank_account = BankAccount.objects.get(account_holder = customer)

    plan = SavingPlan.objects.get(id=plan_id)
    plan.is_current = False
    plan.save()
    deposit_into_account(bank_account.account_number, plan.current_amount)

    return redirect('/home/new_plan/')

