import requests


def get_weather_forecast():
    # connect to weather api
    url = 'http://api.openweathermap.org/data/2.5/weather?'
    url += 'zip=34473,us&units=imperial&APPID=99a1a6d106269f3dd11fe05bc387259d'
    weather_requests = requests.get(url)
    weather_json = weather_requests.json()

    # parsing JSON
    description = weather_json['weather'][0]['description']
    temp_min = weather_json['main']['temp_min']
    temp_max = weather_json['main']['temp_max']

    # creating string
    forecast = 'The Ocala forecast for today is '
    forecast += description + ' with a high of ' + str(int(temp_max))
    forecast += ' and a low of ' + str(int(temp_min)) + '.'

    return forecast
