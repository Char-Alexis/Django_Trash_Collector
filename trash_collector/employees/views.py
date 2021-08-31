# from trash_collector.employees.models import Employees
from trash_collector.customers.models import Customer
from trash_collector import employees
from trash_collector.customers.views import User
from trash_collector.employees.models import Employees
from django.http import HttpResponse
from django.shortcuts import render
from django.apps import app
from .filters import TodaysCustomersFilter

# Create your views here.

# TODO: Create a function for each path created in employees/urls.py. Each will need a template as well.


def index(request):
    # This line will get the Customer model from the other app, it can now be used to query the db for Customers
    Customer = apps.get_model('customers.Customer')
    return render(request, 'employees/index.html')

def filter(request, user_id):
    user = User.objects.get(pk=user_id)
    employees = Employees.objects.get(user=user)
    return render(request, 'employees/filter.html')

customer_filter= TodaysCustomersFilter() 

context = {'customer', 'zip_code', 'weekly_pickup_day', 'one_time_pickup', 'suspend_start', 'suspend_end',
        'customer_filter'
    }
    return render(request, 'update.html', context)

# def update(request, user_id):
#     user = User.objects.get(pk=user_id)
#     customer = Employees.objects.get(user=user)
#      if request.method == 'POST':
#         employees.name = request.POST.get('name')
#         employees.zip_code = request.POST.get('zipcode')
#         return render(request, 'customers/update.html')
        
def update(request, user):
    user= request.user
    logged_in_employee=Employees.objects.get(user=user)
    
    if request.method == 'POST':
        logged_in_employee.name = request.POST.get('name')
        logged_in_employee.zip_code = request.POST.get('zipcode')
        logged_in_employee.user = request.POST.get('user')
        return render(request, 'employees/update.html')

  