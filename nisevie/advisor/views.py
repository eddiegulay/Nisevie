from django.shortcuts import render

from advisor.models import SavingPlan


# Create your views here.
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

