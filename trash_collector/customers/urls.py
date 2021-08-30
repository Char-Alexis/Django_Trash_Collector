from django.urls import path

from . import views

# TODO: Determine what distinct pages are required for the customer user stories, add a path for each in urlpatterns

app_name = "customers"
urlpatterns = [
    path('', views.index, name="index"),
    path('new/', views.create, name="create"),
    path('<int:user_id>', views.detail, name= "detail"),
    path('edit/<int:user_id>', views.update, name="update"),
    path('delete/<int:user_id>', views.delete, name= "delete"),
]
