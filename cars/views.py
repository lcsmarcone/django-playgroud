from django.shortcuts import render
from django.http import HttpResponse
from .models import Car, Brand


# Create your views here.
# def cars_urls(resquest):
#     return render(resquest, 'cars_list.html', {'cars': [
#         {'model': 'Model S', 'brand': 'Tesla', 'factory_year': 2020, 'model_year': 2021, 'value': 79999.99},
#         {'model': 'Mustang', 'brand': 'Ford', 'factory_year': 2019, 'model_year': 2020, 'value': 55999.99}
#     ]})


def cars_urls(request):
    search_query = request.GET.get('search', '')
    # cars = Car.objects.all()  # Busca todos os carros no banco
    cars = Car.objects.filter(model__icontains=search_query).order_by('model')  # Busca carros filtrados pelo modelo
    # cars = Car.objects.filter(model__contains='chevette')  # Busca todos os carros no banco
    return render(request, 'cars_list.html', {'cars': cars})

# def new_car_view(request):
#     if request.method == 'POST':
#         model = request.POST.get('model')
#         brand = Brand.objects.all()
#         factory_year = request.POST.get('factory_year')
#         model_year = request.POST.get('model_year')
#         value = request.POST.get('value')

#         # Aqui você pode adicionar lógica para salvar o novo carro no banco de dados
#         # Exemplo: Car.objects.create(model=model, brand=brand, factory_year=factory_year, model_year=model_year, value=value)

#         return HttpResponse(f'Carro {model} adicionado com sucesso!')

#     return render(request, 'new_car.html')  # Renderiza um template para adicionar um novo carro

def new_car_view(request):
    if request.method == 'POST':
        model = request.POST.get('model')
        brand_id = request.POST.get('brand')  # Pega o ID da marca selecionada
        brand = Brand.objects.get(id=brand_id)  # Busca a instância da marca
        factory_year = request.POST.get('factory_year')
        model_year = request.POST.get('model_year')
        plate = request.POST.get('plate')
        value = request.POST.get('value')
        photo = request.FILES.get('photo')  # para lidar com arquivos

        # Cria o carro no banco
        Car.objects.create(
            model=model,
            brand=brand,
            factory_year=factory_year,
            model_year=model_year,
            plate=plate,
            value=value,
            photo=photo
        )

        return HttpResponse(f'Carro {model} adicionado com sucesso!')

    # GET request — envia a lista de marcas para o template
    brands = Brand.objects.all()
    return render(request, 'new_car.html', {'brands': brands})


def test_base_template(request):
    return render(request, 'base.html')