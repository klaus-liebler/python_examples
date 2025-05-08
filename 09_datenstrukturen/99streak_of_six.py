import random
overall_streaks=0

for experiment in range(10000):
    list = []
    for i in range(100):
        list.append(random.randint(0,1))
    z_or_k=list[0]
    count=1
    for i in range(1,100):
        if(list[i]==z_or_k):
            count+=1
        else:
            count=1
            z_or_k=list[i]
        if count==6:
            overall_streaks+=1
            break
print("Es wurden in", overall_streaks, "der 10000 Experimente ein Sechser-Block gefunden")

