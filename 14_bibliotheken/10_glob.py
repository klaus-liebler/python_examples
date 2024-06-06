import glob

print("Im 'aktuellen' Verzeichnis")
for datei_oder_verzeichnis in glob.glob("*"):
    print(datei_oder_verzeichnis)

for test_datei in glob.glob("glob_test/test??.txt"):
    print(test_datei)

for test_datei in glob.glob("glob_test/test*.txt"):
    print(test_datei)