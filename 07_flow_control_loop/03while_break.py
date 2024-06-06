def execute(str):
    print("Führe aus:", str)

while True:
    code = input("Befehl?")
    if code=='q':
        break
    execute(code)
print('Ende der Verarbeitung')