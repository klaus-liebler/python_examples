def the_list_changer(list):
    list.append("Changed!")

def the_number_changer(number):
    number = number+1

blubb = ["Hallo"]
the_list_changer(blubb)
print(blubb)

zahl=1
the_number_changer(zahl)
print(zahl)

blubb = ["Hallo"]
the_list_changer(blubb.copy())
print(blubb)