Bedingung=False
def Anweisungsblock():
    print()

while Bedingung:
    Anweisungsblock

def execute(str):
    print("Führe aus:", str)

zahl = 1
print('Ich kann schon bis 20 zählen!')
while zahl<=20:
    print(zahl)
    zahl=zahl+1
print('Weiter kann ich noch nicht...')

while True:
    code = input("Befehl?")
    if code=='q':
        break
    execute(code)
print('Ende der Verarbeitung')

while True:
    code = input("Befehl?")
    if code=='q':
        break
    if len(code) < 3:
        print('Eingabefehler!')
        continue;
    execute(code)
print('Ende der Verarbeitung')
