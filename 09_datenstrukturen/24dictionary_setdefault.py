geburtstage ={"Tim":"24.02.2020"}

if "Tom" not in geburtstage:
    geburtstage["Tom"]= "25.02.2020"

geburtstage ={"Tim":"24.02.2020"}

geburtstage.setdefault("Tim", "24.02.2020")
print(geburtstage)
geburtstage.setdefault("Tom", "26.02.2020")
print(geburtstage)