from django.shortcuts import render
from .models import City
from .get_weather import get_weather
from .forms import CityForm


def index(request):
    if request.method == 'POST':
        form = CityForm(request.POST)
        form.save()
    form = CityForm()

    cities = City.objects.all()
    all_cities_data = []
    for city in cities:
        data = get_weather(city.name)
        all_cities_data.append(data)
        context = {'all_info': all_cities_data, 'form': form}
    return render(request, 'weather/index.html', context)
