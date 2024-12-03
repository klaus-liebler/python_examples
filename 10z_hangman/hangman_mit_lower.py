import random
HANGMAN_PICS = ['''
  +---+
      |
      |e
      |
     ===''', '''
  +---+
  O   |
      |
      |
     ===''', '''
  +---+
  O   |
  |   |
      |
     ===''', '''
  +---+
  O   |
 /|   |
      |
     ===''', '''
  +---+
  O   |
 /|\  |
      |
     ===''', '''
  +---+
  O   |
 /|\  |
 /    |
     ===''', '''
  +---+
  O   |
 /|\  |
 / \  |
     ===''']
words = "Umweltschutzorganisation Fussballweltmeisterschaft Nahrungsmittel Liebesabenteuer Sonnenuntergang Haftpflichtversicherung Eintrittskarte Schornsteinfeger Toilettenpapier Taschenmesser".split()

def displayBoard():
    print(HANGMAN_PICS[len(missedLetters)], "\n")
    print('Falsche Buchstaben:', end=' ')
    for letter in missedLetters:
        print(letter, end=" ")
    print()
    for i in range(len(secretWord)):
        if secretWord[i].lower() in correctLetters:
            print(secretWord[i], end=" ")
        else:
            print("_", end=" ")  
    print()

def getGuess():
    # Returns the letter the player entered. This function makes sure the player entered a single letter and not something else.
    while True:
        guess = input("Raten Sie einen Buchstaben! ").lower()
        if len(guess) != 1:
            print('Geben Sie genau einen Buchstaben ein!', end = '')
        elif guess in correctLetters or guess in missedLetters:
            print('Sie haben diesen Buchstaben bereits eingegeben.' , end = '')
        elif guess not in 'abcdefghijklmnopqrstuvwxyzäüöß':
            print('Das war kein Buchstabe! ', end = '')
        else:
            return guess

print('H A N G M A N')
secretWord =  words[random.randint(0, len(words) - 1)]
missedLetters = []
correctLetters = []
while True:
    gameIsDone = False
    displayBoard()
    guess = getGuess()
    if guess in secretWord.lower():
        correctLetters.append(guess)
        foundAllLetters = True
        for i in range(len(secretWord)):
            if secretWord[i].lower() not in correctLetters:
                foundAllLetters = False
                break
        if foundAllLetters:
            print("Hurra! Das geheime Wort lautet \"" + secretWord + "\"! Sie haben gewonnen!")
            gameIsDone = True
    else:
        missedLetters.append(guess)
        if len(missedLetters) == len(HANGMAN_PICS) - 1:
            displayBoard()
            print("Sie haben nach", len(missedLetters), " falschen Buchstaben und", len(correctLetters), "richtigen Buchstaben zu viele Versuche benötigt. Das gesuchte Wort war\"", secretWord,"\"!")
            gameIsDone = True
    if gameIsDone:
        if input("Möchten Sie nochmal spielen? (ja or nein)").lower().startswith('j'):
            secretWord =  words[random.randint(0, len(words) - 1)]
            missedLetters = []
            correctLetters = []
        else:
            break
