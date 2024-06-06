import sqlite3
import requests

request=requests.get('https://api.frankfurter.app/latest', params={'to':'USD'})
parsed_result = request.json()
usd=parsed_result["rates"]["USD"]

conn = sqlite3.connect('bäckerei.db')
c = conn.cursor()
result=c.execute("""SELECT P.name, P.preis_ct, LI.menge, F.ort 
FROM produktstammdaten P
JOIN lagerbestand_ist LI ON LI.produkt_id=P.id
JOIN filialstammdaten F ON LI.filiale_id = F.id
WHERE F.ort="New York" and LI.menge>0""")
for row in result:
    print(f"{row[0]}: {row[1]}EUR-ct --> {row[1]*usd:.2f}US-ct")


conn.close()