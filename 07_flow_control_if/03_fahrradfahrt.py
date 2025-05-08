regenwetter = False
minuten_bis_vorlesungsbeginn = 40
hungerfaktor = 0.3
fahrradfahrt = not regenwetter and (minuten_bis_vorlesungsbeginn < 45 or hungerfaktor > 0.5)
print('Als Wahrheitwert für eine Fahrradfahrt meldet ihr Mobilitäts-KI-System: ', fahrradfahrt)