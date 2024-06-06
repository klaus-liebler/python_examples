from pathlib import Path
from datetime import datetime
import os
todaystr=datetime.now().strftime("%Y%m%d")
root=Path(".", todaystr)
os.makedirs(root)

os.makedirs(root/"Produktion")
os.makedirs(root/"Buchhaltung")
os.makedirs(root/"Sonstiges")

p = Path(".", "Produkte.txt")
produkte=[]
with open(p) as produkt_datei:
    produkte = produkt_datei.readlines()
for p in produkte:
    os.makedirs(root/"Produktion"/p.replace("\"", "_").replace("\n", ""))

p = root/"Buchhaltung"/"liesmich.txt"
p.write_text("Hallo Kolleg*in, bitte die die Buchungsinformationen von "+ todaystr +" ablegen")