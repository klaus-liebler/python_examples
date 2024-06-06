spam=42
cheese = spam
spam=100
print(spam) #100
print(cheese) #42

spam = [0, 1, 2, 3, 4, 5]
cheese = spam
spam[1] = 'Hello!'
print(spam)   #[0, 'Hello!', 2, 3, 4, 5]
print(cheese) #[0, 'Hello!', 2, 3, 4, 5]

