from django.contrib import admin

# Register your models here.


class Filter(admin.SimpleListFilter):
    list_display = ("Monday", "Tuesday", "Wednesday", "Thursday", )

    # request render(admin.SimpleListFilter)