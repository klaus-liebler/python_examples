import time
#Hier fehlt ein Exception-Handling!
time_inp = input("Geben Sie den Timer-Wert im Format min:sec ein")
min = int(time_inp[0:time_inp.find(":")])
sec =int(time_inp[time_inp.find(":")+1:])
print(f"Sie haben {min}:{sec}eingegeben")
secs=60*min+sec;
for i in range(secs, 0,-1):
    print(f"{i//60}:{i%60}")
    time.sleep(1)
print("Ofen öffnen...!")