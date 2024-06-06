def mailtexterzeuger(männlich, name, klausur):
    salution="geehrte Frau"
    artikel="die"
    if(männlich):
        salution="geehrter Herr"
        artikel="der" 
    print("Sehr",salution,"Prof. Dr.",name)
    print("Sie sind", artikel, "beste Prof. aller Zeiten!")
    print("Für eine gute Note in der bevorstehenden", klausur+"-Klausur bedanke ich mich im Voraus.")
    print("Mit größter Bewunderung und freundlichsten Grüßen")
    print("Ihr Student X")
    print("---------------------------------------------------------------------------------------")

mailtexterzeuger(True, "Mentuhotep", "Archäologie")
mailtexterzeuger(False, "Sesostris", "Kulturerbe")
mailtexterzeuger(True, "Uschebti ", "Empirie")
