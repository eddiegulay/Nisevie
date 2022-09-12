from django.shortcuts import render, redirect

from django.contrib.auth.models import User as AccountHolder
from advisor.models import SavingPlan, Stream, StreamCategory
from bankCredentials.models import BankAccount
from .utils import add_stream

#🌟
def home_view(request):
    holder_id = request.user.id
    customer = AccountHolder.objects.get(id=holder_id)
    bank_account = BankAccount.objects.get(account_holder = customer)

    # saving plans 
    saving_plans = SavingPlan.objects.get(target_account = bank_account)
    context = {
        'plans': saving_plans
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
    holder = AccountHolder.objects.get(id=request.user.id) # account holder
    account = BankAccount.objects.get(account_holder = holder) #account linked to income stream
    stream_category = StreamCategory.objects.get(category_name = "Income")# category classification separating Expenses from Incomes

    income_streams = Stream.objects.filter(category= stream_category, linked_account=account)

    context = {
        'income_streams': income_streams
    }
    return render(request, 'advisor/income_streams.html', context)

def advisor_record_expenses(request):
    pass

# 🐛
def PlanCreatorPage(request):
    if request.method == 'POST':
        time_interval = request.POST['interval']
        income_stream = request.POST['income']
        initial_amount = request.POST['amount']
        deposit_frequency = request.POST['frequency']
        new_plan = SavingPlan(time_interval=time_interval,
                              income_stream=income_stream,
                              initial_amount=initial_amount,
                              deposit_frequency=deposit_frequency)
        new_plan.save()

    return render(request, )

