from trash_collector.customers.models import Customer
from django.db.models import fields
import django_filters 
from .models import *
from .views import *

class TodaysCustomersFilter(django_filters.FilterSet):
    class Meta:
        model = Customer
        fields = ['zip_code', 'weekly_pickup_day', 'one_time_pickup', 'suspend_start', 'suspend_end']
    
    
    
    
# customer_filter= TodaysCustomersFilter()

# context = {
#         'days_of_the_week': DayOfTheWeek,
#     }
#     return render(request, 'customers/update.html', context)
