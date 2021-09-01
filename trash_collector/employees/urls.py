from django.urls import path
from .import views

# TODO: Determine what distinct pages are required for the customer user stories, add a path for each in urlpatterns

app_name = "employees"
urlpatterns = [
    path('', views.index, name="index"),
    path('new/', views.create, name="create"),
    path('<int:player_id>/detail', views.detail, name="detail"),
    path('<int:player_id>/update', views.update, name="update"),

    path('filter/', views.filter, name="filter"),
 
]
