import random
def number2name(number):
    if(number==1):
        return "eins"
    elif(number==2):
        return "zwei"
    elif(number==3):
        return "drei"
    else:
        return "die Zahl kann ich nicht"
würfelzahl = random.randint(1,3)
zahlenname = number2name(würfelzahl)
print(zahlenname)
print(number2name(random.randint(1,3)))