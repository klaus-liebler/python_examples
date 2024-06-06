from pathlib import Path
p = Path(".", "badnerlied.txt")

lied_datei = open(p)
lied_inhalt = lied_datei.read()
lied_datei.close()
print(lied_inhalt)

lied_datei = open(p)
lied_inhalt_zeilenweise = lied_datei.readlines()
lied_datei.close()
for liedzeile in lied_inhalt_zeilenweise:
    print("Zeile:", liedzeile, end = '')