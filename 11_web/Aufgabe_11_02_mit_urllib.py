import urllib.parse
import urllib.request
import json
# Die nächsten drei Zeilen sind am Anfang des Programms erforderlich
opener = urllib.request.build_opener()
opener.addheaders = [('User-Agent', 'MyApp/1.0')]
urllib.request.install_opener(opener)

data = {'to':'USD'}
url_values = urllib.parse.urlencode(data)
url = 'https://api.frankfurter.app/latest'
full_url = url + '?' + url_values
print("An den Server wird gesendet:", full_url)
with urllib.request.urlopen(full_url) as response:
    result = response.read()
    print(result)
    parsed_result = json.loads(result)
    city = "US"
    usd=parsed_result["rates"]["USD"]
    print(f"Ein Euro ist {usd:.2f} USD")
