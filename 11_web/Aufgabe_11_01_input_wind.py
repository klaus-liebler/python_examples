import urllib.request
import urllib.parse
import json
import sys

pfeile=["↑", "↗", "→", "↘", "↓", "↙", "←", "↖"]
while(True):
   stadt= input("Geben Sie bitte die Stadt ein oder :q zum Beenden: ")
   if stadt==":q":
      sys.exit()
   data = {'q':stadt, 'APPID':"4a48ca03578c3198f24b59bd2e2e60fd"}
   url_values = urllib.parse.urlencode(data)
   url = 'http://api.openweathermap.org/data/2.5/weather'
   full_url = url + '?' + url_values
   print("An den Server wird gesendet:", full_url)
   try:
      with urllib.request.urlopen(full_url) as response:
         result = response.read()
         parsed_result = json.loads(result)
         city = parsed_result["name"]
         temp=parsed_result["main"]["temp"]-273.15
         wind_deg = parsed_result["wind"]["deg"]
         pfeil=pfeile[int(((wind_deg+22.5)//45)%8)]
         print(f"Die Temperatur in {city} ist {temp:.1f}°C mit Wind {wind_deg} {pfeil}")
   except urllib.error.HTTPError as e:
      print(f"Da lief etwas schief, nämlich {e}... Bitte nochmal!")

