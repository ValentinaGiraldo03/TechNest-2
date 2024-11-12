from django.shortcuts import render
from product.models import Product
from django.utils.translation import gettext as _

import requests
from django.shortcuts import render

def home_view(request):
    api_key = ""
    city = "Medellin"
    weather_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric&lang=es"

    response = requests.get(weather_url)
    if response.status_code == 200:
        weather_data = response.json()
        weather = { 
            'description': weather_data['weather'][0]['description'],
            'temperature': weather_data['main']['temp'],
            'city': city
        }
    else:
        weather = None

    filter = request.GET.get('filter')
    if filter:
        products = Product.objects.filter(name__icontains=filter)
    else:
        products = Product.objects.all()

    return render(request, 'home.html', {'products': products, 'weather': weather})
