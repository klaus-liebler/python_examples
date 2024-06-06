zahlen =[45,2,36,15]
zahlen.sort()
print(zahlen) #[2, 15, 36, 45]

namen=["Bär", "Igel", "Affe"]
namen.sort()
print(namen) #['Affe', 'Bär', 'Igel']

namen=["Biber", "adler"]
print(namen.sort()) #['Biber', 'adler']
print(namen.sort(key=str.casefold)) #['adler', 'Biber']

test = ["2","1", "Gnu", "Emu"]
print(test.sort(reverse=True)) #['Gnu', 'Emu', '2', '1']

test = [2,1, "Yak", "Zebra"]
test.sort() #TypeError!