import time
import datetime
import urllib.request
import urllib.parse
import json
import sys
data = {}
data['q'] = 'Osnabrück'
data['APPID'] ="4a48ca03578c3198f24b59bd2e2e60fd"
url_values = urllib.parse.urlencode(data)
url = 'http://api.openweathermap.org/data/2.5/forecast'
full_url = url + '?' + url_values
print(full_url)

unixtime = int(time.time())+(24*60*60)

with urllib.request.urlopen(full_url) as response:
    result = response.read()
    parsed_result = json.loads(result)
    city = parsed_result["city"]["name"]
    forecast24h = None
    for forecast in parsed_result["list"]:
        if forecast["dt"]>unixtime:
           forecast24h=forecast
           break
    if forecast24h != None:
        temp=forecast24h["main"]["temp"]-273.15
        date = datetime.datetime.fromtimestamp(forecast24h["dt"])
        print(f"In {city} wird am {date:%d.%m.%Y} um {date:%H:%M} eine Temperatur von {temp:.2f}°C erwartet")
    else:
        print("Keine Vorhersage für Morgen gefunden")