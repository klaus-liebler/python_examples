import numpy as np

a = np.array([[0, 1, 2, 3, 4, 5],[10,11,12,13,14,15],[20,21,22,23,24,25],[30,31,32,33,34,35],[40,41,42,43,44,45],[50,51,52,53,54,55]])
print("Erstens")
print(a[(0,1,2,3,4),(1,2,3,4,5)])
print("Zweitens")
print(a[3:,[0,2,5]])
print("Drittens")
mask=np.array([1,0,1,0,0,1], dtype=bool)
print(a[mask,2])
print()

print("Viertens")
print(a[np.array([0,0,0,1,0,1], dtype=bool), 3:])



