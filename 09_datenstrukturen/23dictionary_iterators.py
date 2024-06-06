geburtstage={"Klaus":"6.8.","Klara":"2.8."}

for v in geburtstage.values():
    print(v)

for k in geburtstage.keys():
    print(k,"hat am",geburtstage[k])

for i in geburtstage.items():
    print(i[0], "hat am", i[1])

for k,v in geburtstage.items():
    print(k,"hat am",v)
