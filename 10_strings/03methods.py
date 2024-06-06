test = "Hallo Welt"
print("allo" in test) #True
print(test.startswith("Hallo")) #True
print(test.endswith("elt")) #True
print(test.find("W")) #6


test = "hAlLo WElt"
print(test.lower()) #wandelt alles in Kleinbuchstaben um
print(test.upper()) #macht alles groß
print(test.lower().islower()) #prüft, ob alles klein ist
print(test.upper().isupper()) #prüft, ob alles groß ist



items = "Mein Name ist Klaus".split()
print(items) #['Mein', 'Name', 'ist', 'Klaus']
text = "%$%".join(items)
print(text) #Mein%$%Name%$%ist%$%Klaus



print("AbC".isalpha())
print("A b C".isalpha())
print("123".isalpha())

print("ABc".isalnum())
print("A B c".isalnum())
print("123.0".isalnum())
print("1A2b3".isalnum())

print("123".isdecimal())
print("123.0".isdecimal())