klümpchenanzahl = 10
cross = True
backzeitMinuten=0
def rühren():
    global klümpchenanzahl
    print("rühren")
    klümpchenanzahl-=1

def NimmTeigUndFormeBallen(i):
    print("NimmTeigUndFormeBallen" + str(i))

def TrenneEier():
    print("Trenne Eier")

def RühreEinweißSchaumig():
    print("Trenne Eier")

def HebeEischneeUnter():
    print("HebeEischneeUnter")

TrenneEier()
RühreEinweißSchaumig()
HebeEischneeUnter()

while(klümpchenanzahl > 0):
    rühren()

if(cross==True):
    backzeitMinuten=18 
else:
     backzeitMinuten=15

for i in range(0, 6):
    NimmTeigUndFormeBallen(i)

def f(x):
    return x*x+4*x+1

y=f(3)
print(y)