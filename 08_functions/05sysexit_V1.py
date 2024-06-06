import sys
cmd1 = input("Bitte geben Sie ein Kommando ein: ")
if len(cmd1)<3:
    print("Ungültiges Kommando!")
    sys.exit()
print("Ich mache jetzt", cmd1)


