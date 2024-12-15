import requests
request=requests.get("https://api.frankfurter.app/latest", params={'to':'USD'})
print("An den Server wird gesendet:", request.url)
parsed_result = request.json()
usd=parsed_result["rates"]["USD"]
print(f"Ein Euro ist aktuell {usd} USD")

