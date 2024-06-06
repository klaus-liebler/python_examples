allGuests = {'Alfons': {'Äpfel': 5, 'Bretzeln': 12},
             'Bettina': {'Wurstbrötchen': 3, 'Äpfel': 2},
             'Christian': {'Tassen': 3, 'Apfelkuchen': 1}}

def totalBrought(dictOfDict):
    overview = {}
    for broughtDictionary in dictOfDict.values():
        for thing, count in broughtDictionary.items():
            currentCount=overview.get(thing,0)
            overview[thing] = currentCount+count
    return overview

print("Liste der insgesamt mitgebrachten Dinge")
for k, v in totalBrought(allGuests).items():
        print(" -", k, ":", v)
