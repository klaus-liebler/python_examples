print("Einmaleins in wählbarer Größe")
rangeend=21
for i in range(1,rangeend):
    for j in range(1,rangeend):
        prod=i*j
        print(f'{prod:4}', end="")
    print()
print("Das wars...")


