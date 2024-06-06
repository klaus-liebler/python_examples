zutaten = ["Mehl", "Eier", "Milch", "Zucker"]
for i in zutaten:
    print(i)
for i in range(len(zutaten)):
    print("Die "+str(i)+". Zutat ist:", zutaten[i])
for index, item in enumerate(zutaten):
    print("Die "+str(index) +". Zutat ist", item)