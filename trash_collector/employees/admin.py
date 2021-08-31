from django.contrib import admin

# Register your models here.

# Filter method as a class or seperate file?

class Filter(admin.SimpleListFilter):
    list_display = ("Monday", "Tuesday", "Wednesday", "Thursday", )

    # request render(admin.SimpleListFilter)