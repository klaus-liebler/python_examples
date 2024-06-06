# Dieses Programm begrüßt Sie und trifft eine Aussage zu Ihrem Alter
print("Hallo, lieber Computernutzer")
userName = input('Wie ist Ihr Name? ') #Frage nach dem Name
userAge = input('Wie als sind Sie? ') #Frage nach dem Alter
print('Schön, Sie kennen zu lernen,', userName)
print('Ihr Name besteht aus', len(userName), 'Buchstaben')
userAge_plus_1 = int(userAge)+1
print('In einem Jahr werden Sie', userAge_plus_1 , 'Jahre als sein.')