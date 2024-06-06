kalt = True
regen = True
sonnenschein = False
print('Dass es einen Regenbogen gibt, ist', regen and sonnenschein)
print('Dass es warm ist, ist', not kalt)
print('Dass die gute Outdoor-Jacke notwendig ist, ist', kalt or regen)