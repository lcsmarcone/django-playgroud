from django.shortcuts import render
from django.http import HttpResponse
from .models import Car


# Create your views here.
# def cars_urls(resquest):
#     return render(resquest, 'cars_list.html', {'cars': [
#         {'model': 'Model S', 'brand': 'Tesla', 'factory_year': 2020, 'model_year': 2021, 'value': 79999.99},
#         {'model': 'Mustang', 'brand': 'Ford', 'factory_year': 2019, 'model_year': 2020, 'value': 55999.99}
#     ]})


def cars_urls(request):
    cars = Car.objects.all()  # Busca todos os carros no banco
    return render(request, 'cars_list.html', {'cars': cars})
