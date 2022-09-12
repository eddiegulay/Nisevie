from django.shortcuts import render

from django.contrib.auth.models import User as AccountHolder
from advisor.models import SavingPlan
from bankCredentials.models import BankAccount

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

# 🐛
def advisor_view(request):
    return render(request, 'advisor.html')


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

