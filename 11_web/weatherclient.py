import urllib.request
import urllib.parse
import json

data = {'q':'Greven', 'APPID':"4a48ca03578c3198f24b59bd2e2e60fd"}
url_values = urllib.parse.urlencode(data)
url = 'http://api.openweathermap.org/data/2.5/weather'
full_url = url + '?' + url_values
print("An den Server wird gesendet:", full_url)
with urllib.request.urlopen(full_url) as response:
   result = response.read()
   parsed_result = json.loads(result)
   city = parsed_result["name"]
   temp=parsed_result["main"]["temp"]-273.15
   print(f"Die Temperatur in {city} ist {temp:.1f}°C")
