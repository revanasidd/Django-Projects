from email import message
from django.shortcuts import render
import requests
import datetime

# Create your views here.
def weather(request):
    try:
        city=request.POST.get('city', 'Bengaluru')
        if city == '':
            url=f'http://api.openweathermap.org/data/2.5/weather?q=Bengaluru&appid=1f77aaadc276c1bcc350c60b812f1447'
        else:
            url=f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid=1f77aaadc276c1bcc350c60b812f1447'
    
        data=requests.get(url).json()
        print(data)
        payload={
            'wind': data['wind']['speed'],
            'country': data['sys']['country'],
            'city': data['name'],
            'description': data['weather'][0]['description']
        }
        context={'data': payload}
        return render(request, 'weather.html', context)
    except Exception as ValueError:
        message.warning('city you mentioned wrong')

def base(request):
    return render(request, 'base.html')