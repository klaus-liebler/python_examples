import matplotlib.pyplot as plt
days=[0,3,7,13,17,22,28,31]
celsius_min=[19.6, 24.1,26.7,28.3,27.5,30.5,32.8,33.1]
celsius_max=[24.8, 28.9, 31.3, 33.0, 34.9, 35.6, 38.4, 39.2]
plt.xlabel("Tag")
plt.ylabel("Temperatur [Grad]")
plt.plot(days, celsius_min)
plt.plot(days,celsius_min, "oy", label="Minimal")
plt.plot(days, celsius_max)
plt.plot(days,celsius_max, "or", label="Maximal")
plt.legend()
plt.show()

