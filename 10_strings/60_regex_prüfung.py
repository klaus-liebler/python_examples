import re
regex = r"[a-z][A-Z]{2,2}[a-z]{1,}[1-9]{0,}"
regex=re.compile(regex)
test="AzzABzz"
print(regex.search(test))
test="aAaAa-z1-9"
print(regex.search(test))
test="1aAAa1"
print(regex.search(test))
test="KlausLiebler"
print(regex.search(test))
test="DV1"
print(regex.search(test))
test="\t\t  tRAa\n"
print(regex.search(test))