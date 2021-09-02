from django.urls import path

from . import views

# TODO: Determine what distinct pages are required for the customer user stories, add a path for each in urlpatterns

app_name = "customers"
urlpatterns = [
    path('', views.index, name="index"),
    path('new/', views.create, name="create"),
    path('<int:user_id>/detail', views.detail, name= "detail"),
    path('<int:user_id>/edit', views.update, name="update"),
    path('<int:user_id>/delete', views.delete, name= "delete"),
]
