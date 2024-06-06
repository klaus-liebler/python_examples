def OfenEinstellen(grad):
    print("Ofen auf ", grad, "°C einstellen")
def OfenVorheizen():
    print("Warte, bis Temperatur erreicht ist")
    Warten()
def BackwarenEinschieben():
    OfenÖffnen()
    Einschieben()
    OfenSchließen()
def OfenÖffnen():
    print("Ofen öffnen")
def Einschieben():
    print("Backwaren einschieben")
def OfenSchließen():
    print("Klappe zu!")
def BackwarenRausholen():
    print("Backwaren rausholen!")

def Warten(t):
    print("Warte", t, " Minuten")
    print("dudidadidödeldü...")
    print("tirilitirila...")
    print("Feeertig!!!")
def PlätzchenBacken(grad, zeit):
  OfenEinstellen(grad)
  Warten(5)
  BackwarenEinschieben()
  Warten(zeit)
  BackwarenRausholen()

def Anweisungsblock1():
    print()
def Anweisungblock2():
    print()   
def Anweisungsblock3():
    print()
def Anweisungsblock4():
    print()   
def Bedingung1():
    Bedingung1=True
def Bedingung2():
    Bedingung2=True
def Bedingung3():
    Bedingung3=True

zucker_multiplikator = 0

süße = input("Wie süß sollen die Plätzchen werden?")
if süße == "süß":
	zucker_multiplikator=1.2
elif süße == "gesund":
	zucker_multiplikator=0.8
else:
	zucker_multiplikator=1
print("Zuckermultiplikator ", zucker_multiplikator)

if Bedingung1:
    Anweisungsblock1
elif Bedingung2:
    Anweisungsblock2
elif Bedingung3:
    Anweisungsblock3
else:
    Anweisungsblock4

PlätzchenBacken(180, 15)