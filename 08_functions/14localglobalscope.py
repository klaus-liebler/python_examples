def aaa1():
    print("Die globale Var. a hat den Wert ", a)
    c=100
    print("Die lokale Variable c hat den Wert ", c)
    return None

def aaa2():
    global a #Ist nur nötig, wenn man glob. Var. beschreiben möchte
    print("Globale Var. a vor lokaler Veränderung ", a)
    a=a+1
    print("Globale Var. a nach lokaler Veränderung ", a)

def bbb():
    b=11
    print("Die glob. Var. b wird lok. überdeckt. Lok. Wert:", b)
    #print(c) #Dies wäre ein Fehler. c ist hier nicht gültig.
a=2 #das ist die globale Variable a
b=10 #das ist die globale Variable b
aaa1()
aaa2()
print("GlobalScope: Globale Var. a", a)
bbb()
print("Die globale Var. existiert weiterhin. Wert ", b)
#print(c) #Dies wäre ein Fehler. c ist global nicht gültig.


