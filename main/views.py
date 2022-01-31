# Create your views here.
from django.shortcuts import render
import json
from .models import Weather
import urllib.request


def index(request):
    if request.method == 'POST':
        city = request.POST['city']

        source = urllib.request.urlopen(
             'http://api.openweathermap.org/data/2.5/weather?q='
                    + city + '&appid=ee813bcfef3f7f2c1e3099e0e95da065').read()

        list_of_data = json.loads(source)

        data = {
            "country_code": str(list_of_data['sys']['country']),
            "coordinate": str(list_of_data['coord']['lon']) + '' + str(list_of_data['coord']['lat']),
            "temp": str(list_of_data['main']['temp']) + 'k',
            "pressure": str(list_of_data['main']['pressure']),
            "humidity": str(list_of_data['main']['humidity']),

    }
        context = Weather(city=city,temp=data["temp"])
        context.save()
        print(data)
        # 
        # # print ("sent")

    else:
        data = {}

    return render(request, "index.html", data)



def search(request):
    context = Weather.objects.all()
    
    updated_data = context.reverse()[::-1]
    
    return render(request, "history.html",{'context':updated_data})