# Dies ist ein Nummern-Rate-Spiel
import random, sys
secretNumber = random.randint(1, 20)
print("Ich habe mir gerade eine Zahl zwischen 1 und 20 ausgedacht :-)")
max_guesses = int(input("Wie viele Rateversuche brauchen Sie? "))
# Der Spieler darf sechsmal raten (range = exklusive dem Ende)
for guessesTaken in range(1, max_guesses+1):
    guess = int(input("Raten Sie mal! "))
    if guess < secretNumber:
        print("Zu klein!")
    elif guess > secretNumber:
        print("Zu groß!")
    else:
        print('Gut gemacht. Sie haben die richtige Zahl nach', guessesTaken, " Versuchen erraten.")
        sys.exit()
print('Leider haben Sie es nicht geschafft! Meine geheime Zahl war', secretNumber, '.')