from django import forms

from .models import Customer

class CustomerUpdateForm(forms.ModelForm):

    class Meta:
        model = Customer
        fields = ['weekly_pickup_day', 'one_time_pickup', 'suspend_start', 'suspend_end']