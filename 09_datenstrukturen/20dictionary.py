telefonbuch = {'Tick':'3412', 'Trick': '8392', 'Track': '8493'}
print(telefonbuch["Track"]) #'8493'

print(telefonbuch["Donald"]) #KeyError                                           
telefonbuch["Donald"]="5555"
print(telefonbuch["Donald"]) #'5555'
