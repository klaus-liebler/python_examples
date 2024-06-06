def collatz(number):
    print(number)
    if number%2==0:
        return number//2
    else:
        return 3*number+1

x = -1
while x<1:
    try:
        x=int(input("Geben Sie eine ganze positive Zahl ein: "))
    except ValueError:
        print("Falsche Eingabe!")
while x!=1:
    x=collatz(x)
print(x)

