Bedingung=False
def Anweisungsblock():
    print()

while Bedingung:
    Anweisungsblock

def execute(str):
    print("Führe aus:", str)


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
