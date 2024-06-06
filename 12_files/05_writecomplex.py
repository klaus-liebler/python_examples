from pathlib import Path
from datetime import datetime
p = Path(".", "bratkartoffel_zeit.txt")
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")



bratkartoffel_datei = open(p, 'w')   
bratkartoffel_datei.write('Hallo Bratkartoffel!\n')
bratkartoffel_datei.close()

bratkartoffel_datei = open(p, 'a')
bratkartoffel_datei.write("Es ist jetzt " + timestamp + "\n")
bratkartoffel_datei.write("Und jetzt ist Schluss\n")
bratkartoffel_datei.close()

print(p.read_text())
