# Wenn es nicht regnet und es weniger als 45min bis Vorlesungsbeginn ist oder ich großen Hunger (auf Mensaessen) habe,
# dann fahre ich jetzt mit dem Fahrrad zur Hochschule

regenwetter = False
minuten_bis_vorlesungsbeginn = 40
hungerfaktor = 0.3
fahrradfahrt = not regenwetter and (minuten_bis_vorlesungsbeginn < 45 or hungerfaktor > 0.5)
print('Als Wahrheitwert für eine Fahrradfahrt meldet ihr Mobilitäts-KI-System: ', fahrradfahrt)