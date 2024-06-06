name = input("Your Name? ")
password = input("Your password? ")
if name == 'Mary':
    print('Hello, Mary')
    if password == 'swordfish':
        print('Access granted.')
        task = input('What would you like me to do today?: ')
        print('OK, so I do '+task+' all day long.')
    else:
        print('Wrong password.')
else:
    print("I do not know you!")


