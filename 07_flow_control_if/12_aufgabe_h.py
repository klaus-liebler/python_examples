#h)	Schreiben Sie eine if-elif-else-Anweisung, die das Folgende tut (Annahme: es existiert eine Integer-Variable „zahl“) 
#1)	Es soll „A“ ausgegeben werden, wenn „zahl“ ohne Rest durch 2 und 3 teilbar ist (Modulo-Operator ist %) und die Zahl größer als 10 ist
#2)	Es soll „B“ ausgegeben werden, das obige nicht zutrifft, aber wenn „zahl“ zumindest eine gerade Zahl ist
#3)	Wenn das alles nicht zutrifft, soll „C“ ausgegeben werden.
zahl=12
if zahl%2==0 and zahl%3==0 and zahl>10:
    print("A")
elif zahl%2==0:
    print("B")
else:
    print("C")