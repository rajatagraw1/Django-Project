from django.urls import path
from .views import calculate_cost,index

urlpatterns = [
    path('', index, name='index'),
    path('calculate/', calculate_cost, name='calculate_cost'),
]