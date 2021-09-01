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
from django.shortcuts import render
from django.apps import apps
from django.urls import reverse
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
        not_suspended_customers = Customer.objects.filter()
        
        # find customers with pickupday tihs day or one time pickup today
        # todays_customers = zip_code_customers.filter()
        return render(request, 'employees/index.html')
    except:
        # TODO: Redirect the user to a 'create' function to finish the registration process if no customer record found
        return HttpResponseRedirect('employees:create')

def create(request):
    # user = request.user
    # logged_in_employee = Employees.objects.get(user=user)
    if request.method == "POST":
        name = request.POST.get('name')
        zip_code = request.POST.get('zip_code')
        user = request.POST.get('user')
        new_employees = Employees (name=name, zip_code=zip_code)
        new_employees.save()
        return HttpResponseRedirect(reverse('employees:index'))
    else:
        # Employees= apps.get_model('employees.Employees')
        # all_employees= Employees.object.all()
        return render(request,'employees/create.html')

def detail(request, user_id):
    employees_from_db = Employees.objects.get(pk=user_id)
    return render(request, 'employees/detail.html', {'employees': employees_from_db})



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

  