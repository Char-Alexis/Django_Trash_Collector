# # from trash_collector.employees.models import Employees
# from django.http.response import HttpResponseRedirect
# # from trash_collector.customers.models import Customer
# # from trash_collector.customers.views import User
# from trash_collector.employees.models import Employees
# from django.http import HttpResponse
# from django.shortcuts import render
# from django.apps import apps
from .models import Employees
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.apps import apps
from django.urls import reverse
from datetime import date
# Create your views here.

# TODO: Create a function for each path created in employees/urls.py. Each will need a template as well.


def index(request):
    # This line will get the Customer model from the other app, it can now be used to query the db for Customers
    Customer = apps.get_model('customers.Customer')

        # The following line will get the logged-in in user (if there is one) within any view function
    user = request.user

    try:
        # This line inside the 'try' will return the customer record of the logged-in user if one exists
        logged_in_employee = Employees.objects.get(user=user)
        # find logged in employee so we can get their zip code
        # find all customers in employee's zip code
        zip_code_customers = Customer.objects.filter(zip_code=logged_in_employee.zip_code)
        # find all customers who are not suspended
        todays_date = date.today()
        active_customers = []
        for customer in zip_code_customers:
            if customer.suspend_start < todays_date and customer.suspend_end > todays_date:
                pass
            else:
                active_customers.append(customer)
                
        # find customers with pickupday tihs day or one time pickup today
        # todays_customers = active_customers.objects.filter()

        todays_customers = []
        for customer in active_customers:
            if customer.weekly_pickup_day == todays_date or customer.one_time_pickup == todays_date:
                todays_customers.append(customer)
            else:
                pass
        
        context = {
            'todays_customers': todays_customers
        }
        return render(request, 'employees/index.html', context)

    except:
        # TODO: Redirect the user to a 'create' function to finish the registration process if no customer record found
        return HttpResponseRedirect(reverse('employees:create'))

def filter(request):
        

        return render(request, 'employees/filter.html')


def create(request):
    # user = request.user
    # logged_in_employee = Employees.objects.get(user=user)
    if request.method == "POST":
        name = request.POST.get('name')
        zip_code = request.POST.get('zip_code')
        new_employees = Employees (name=name, user=request.user, zip_code=zip_code)
        new_employees.save()
        return HttpResponseRedirect(reverse('employees:index'))
    else:
        return render(request,'employees/create.html')

def detail(request, user_id):
    employees_from_db = Employees.objects.get(pk=user_id)
    return render(request, 'employees/detail.html', {'employees': employees_from_db})


def update(request, user):
    user= request.user
    logged_in_employee=Employees.objects.get(user=user)
    
    if request.method == 'POST':
        logged_in_employee.name = request.POST.get('name')
        logged_in_employee.zip_code = request.POST.get('zip_code')
        logged_in_employee.user = request.POST.get('user')
        logged_in_employee.save()
        return redirect (request, 'employees:update.html')


  