zutaten = ["Mehl", "Eier"]
zutaten.append("Zucker")
zutaten.append("Milch")
print(zutaten)

zutaten = ["Mehl", "Eier"]
zutaten.insert(1, "Zucker")
zutaten.insert(1, "Milch")
print(zutaten)

zutaten=["Mehl", "Eier", "Milch", "Eier"]
zutaten.remove("Eier")                    
print(zutaten) #['Mehl', 'Milch', 'Eier']
zutaten.remove("Schokolade") #ValueError!
