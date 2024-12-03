print("Einmaleins in wählbarer Größe")
rangeend=15
for i in range(1,rangeend):
    for j in range(1,rangeend):
        prod=i*j
        #print(f'{prod:4}', end="")
        if prod<10:
            print("  ", prod, end="")
        elif prod<100:
            print(" ", prod, end="")
        else:
            print("", prod, end="")
    print("")
print("Das wars...")


