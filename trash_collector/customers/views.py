# from trash_collector.employees.filters
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import Customer
from .choices import DayOfTheWeek
from .forms import CustomerUpdateForm


# Create your views here.

# TODO: Create a function for each path created in customers/urls.py. Each will need a template as well.

User = get_user_model()

def index(request):
    # The following line will get the logged-in in user (if there is one) within any view function
    user = request.user

    try:
        # This line inside the 'try' will return the customer record of the logged-in user if one exists
        logged_in_customer = Customer.objects.get(user=user)
    except:
        # TODO: Redirect the user to a 'create' function to finish the registration process if no customer record found
        return HttpResponseRedirect('customers:create')

    # It will be necessary while creating a Customer/Employee to assign request.user as the user foreign key
    return render(request, 'customers/index.html')


def create(request):
    user = request.user

    if request.method == "POST":
        name = request.POST.get('name')
        address = request.POST.get('address')
        zip_code = request.POST.get('zipcode')
        balance = request.POST.get('balance')
        weekly_pickup_day = request.POST.get('weekly pickup day')
        one_time_pickup = request.POST.get('one time pickup')
        suspend_start = request.POST.get('suspend start')
        suspend_end = request.POST.get('suspend end')
        new_customer = Customer(name=name, user=user, address=address, zip_code=zip_code, balance=balance, weekly_pickup_day=weekly_pickup_day, one_time_pickup= one_time_pickup, suspend_start=suspend_start, suspend_end=suspend_end)
        new_customer.save()
        return HttpResponseRedirect(reverse('customers:index'))
    context = {
        'days_of_the_week': DayOfTheWeek,
    }
    return render(request, 'customers/create.html', context)


def detail(request, user_id):
    logged_in_customer = Customer.objects.get(pk=user_id)
    context = {
        'logged_in_customer': logged_in_customer
    }
    return render(request, 'customers/detail.html',  context)


def update(request, user_id):
    user = User.objects.get(pk=user_id)
    customer = Customer.objects.get(user=user)
    form = CustomerUpdateForm(instance=customer)
    
    if request.method == 'POST':
        form = CustomerUpdateForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('customers:index')


        context = {
            'days_of_the_week': DayOfTheWeek,
            'form': form,
        }
        return render(request, 'customers/update.html', context)


def delete(request, user_id):
    customer_from_db = Customer.objects.get(pk=user_id)
    customer_from_db.delete()
    return render(request, 'customers/delete.html')