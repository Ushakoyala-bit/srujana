from django.shortcuts import render
from django.contrib import messages
import requests
import datetime

def home(request):
    if 'city' in request.POST:
        city = request.POST['city']
    else:
        city = 'hyderabad'
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=6749f5969faad9dc74e2a8dfaac8be5e'
    PARAMS = {'units': 'metric'}

    API_KEY = 'AIzaSyCAwCW9aI17jkDeARBVOcYfm3MmGU7If5s'
    SEARCH_ENGINE_ID = '26cd83dd9c4724988'
    query = city + "1920*1080"
    page = 1
    start = (page - 1) * 10 + 1
    searchtype = 'image'
    city_url = f"https://www.googleapis.com/customsearch/v1?key={API_KEY}&cx={SEARCH_ENGINE_ID}&q={query}&start={start}&searchtype={searchtype}&imgsize=xlarge"

    data = requests.get(city_url).json()
    count = 1
    search_items = data.get("items")
    image_url = search_items[1]['link'] if search_items and len(search_items) > 1 else None

    try:
         data = requests.get(url,params=PARAMS).json()

         description = data['weather'][0]['description']
         icon=data['weather'][0]['icon']
         temp=data['main']['temp']

         day=datetime.date.today()

    
         return render(request,'weatherapp/index.html',{'description':'clear sky','icon':'01d','temp':25,'day':day,'city':'hyderabad','exception_occured':False,'image_url':image_url})
    except:
        exception_occured=True
        messages.error(request,'entered data is not available to API')
        day=datetime.date.today()
        
        return render(request,'weatherapp/index.html',{'description':'clear sky','icon':'01d','temp':25,'day':day,'city':'hyderabad','exception_occured':True,})
