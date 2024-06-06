def execute(cmd):
    print("Führe aus:", cmd)

command_executions = 0
while command_executions<4:
    command = input("Kommando?")
    if command=='q':
        break
    if len(command) < 3:
        print('Eingabefehler!')
        continue
    execute(command)
    command_executions=command_executions+1
print('Ende der Kommando-Verarbeitung')
