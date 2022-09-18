from django.shortcuts import render, redirect

from django.contrib.auth.models import User as AccountHolder
from advisor.models import SavingPlan, Stream, StreamCategory
from bankCredentials.models import BankAccount,ServiceRequirements, BankService, ServiceBenefit
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
    holder = AccountHolder.objects.get(id=request.user.id)  # account holder
    account = BankAccount.objects.get(account_holder=holder)  # account linked to income stream

    if request.POST:
        stream_name = request.POST['stream_name']
        stream_amount = request.POST['stream_amount']
        time_interval = request.POST['time_interval']
        stream_frequency = request.POST['stream_frequency']

        add_stream(
            _linked_account=account.id, 
            is_expense=False, 
            _name=stream_name, 
            _amount=stream_amount, 
            _tag=stream_frequency, 
            _interval=time_interval, 
            _can_save=0, 
            _least_expenditure=0, 
            _time_delay=0)

        return redirect('/home/streams/')

    # active income streams
    
    stream_category = StreamCategory.objects.get(
        category_name="Income")  # category classification separating Expenses from Incomes

    income_streams = Stream.objects.filter(category=stream_category, linked_account=account)

    context = {
        'income_streams': income_streams
    }
    return render(request, 'advisor/income_streams.html', context)


def advisor_record_expenses(request):
    holder = AccountHolder.objects.get(id=request.user.id)  # account holder
    account = BankAccount.objects.get(account_holder=holder)  # account linked to income stream
    if request.POST:
        stream_name = request.POST['stream_name']
        stream_amount = request.POST['stream_amount']
        time_interval = request.POST['time_interval']
        stream_frequency = request.POST['stream_frequency']
        can_save_amount = request.POST['can_save_amount']
        least_expenditure = request.POST['least_expenditure']

        add_stream(
            _linked_account=account.id, 
            is_expense=True, 
            _name=stream_name, 
            _amount=stream_amount, 
            _tag=0, 
            _interval=time_interval, 
            _can_save=can_save_amount, 
            _least_expenditure=least_expenditure, 
            _time_delay=0)

        return redirect('/home/expenses/')

    # active expense streams
    
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



def delete_income_stream(request, _id):
    stream = Stream.objects.get(id=_id)
    stream.delete()

    return redirect("/home/streams/")


def edit_income_stream(request, _id):
    stream = Stream.objects.get(id=_id)
    if request.POST:
        stream.name = request.POST['stream_name']
        stream.amount = request.POST['stream_amount']
        stream.time_interval = request.POST['time_interval']
        stream.tag = request.POST['stream_frequency']
        stream.can_save_amount = request.POST['can_save_amount']
        stream.least_expenditure = request.POST['least_expenditure']

        stream.save()
        return redirect('/home/streams/')

    context = {
        'expense': stream
    }
    return render(request, 'advisor/edit_income.html', context)


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
    income_expense_difference = total_income - total_expenses

    # default recommendation data
    opt_loans = 0
    loan_data_bucket = []
    if income_expense_difference <= 0:
        loan_requirements = ServiceRequirements.objects.filter(minimum__lte=income_expense_difference, maximum__gte=income_expense_difference)
        opt_loans = len(loan_requirements)
        if opt_loans >= 1:
            loan_data_bucket = []
            for loan in loan_requirements:
                recommended_loans = BankService.objects.filter(id = loan.parent_service.id)
                for loan_item in recommended_loans:
                    loan_requirements = ServiceRequirements.objects.filter(parent_service = loan_item)
                    loan_benefits = ServiceBenefit.objects.filter(parent_service = loan_item)
                    loan_data_bucket.append(
                        {
                            'loan': loan_item,
                            'requirements': loan_requirements,
                            'benefits': loan_benefits
                        }
                    )

    
    context = {
        'funds_difference': income_expense_difference,
        'total_income': total_income,
        'total_expense': total_expenses,
        'expense_list': expense_list,
        'income_list': income_list, 
        'loans_availbale': opt_loans,
        'loan_data_bucket': loan_data_bucket
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
        end_date = request.POST['end_date']
        plan_name = request.POST['plan_name']
        is_fixed = request.POST['is_fixed']
        income = Stream.objects.get(id= income_stream)

        if int(is_fixed) == 1:
            is_fixed = True
        else:
            is_fixed = False
            
        # move funds from main balance to savings
        condition = withdraw_from_account(bank_account.account_number, initial_amount)
        if condition:
            new_plan = SavingPlan(plan_name=plan_name, target_account = bank_account,time_interval=time_interval, income_stream=income, current_amount=initial_amount, frequency_deposit_amount=initial_amount, is_active=True, allowed_withdraw_date=end_date, is_fixed=is_fixed)
            new_plan.save()
        else:
            new_plan = SavingPlan(plan_name=plan_name, target_account = bank_account,time_interval=time_interval, income_stream=income, current_amount=0, frequency_deposit_amount=initial_amount, is_active=True, allowed_withdraw_date=end_date, is_fixed=is_fixed)
            new_plan.save()
        
        return redirect('.')

    return render(request, 'advisor/create_plan.html', {'plans': saving_plans, 'streams': income_list})


def plans_view(request):
    holder_id = request.user.id
    customer = AccountHolder.objects.get(id=holder_id)
    bank_account = BankAccount.objects.get(account_holder=customer)

    # saving plans 
    saving_plans = SavingPlan.objects.filter(target_account=bank_account)
    active_plans = SavingPlan.objects.filter(target_account=bank_account, is_active=True)
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
    plan.is_active = False
    plan.save()
    deposit_into_account(bank_account.account_number, plan.current_amount)

    return redirect('/home/new_plan/')

