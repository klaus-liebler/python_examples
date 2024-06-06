import math
from script_nonsense import nonsense as n

def hallo_auf_spanisch():
    return "Hola"

def Umfang(radius):
    return math.pi*2*radius

if __name__ == "__main__":
    n()
    print(hallo_auf_spanisch())
    print ("Radius=2, Umfang=", Umfang(2))