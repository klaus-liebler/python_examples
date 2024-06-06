import numpy as np
ein_1D_array=np.array([7,2,9,10])
print(ein_1D_array)
print(ein_1D_array.shape)
print()

ein_2D_array = np.array([[5.2, 3.0, 4.5],[9.1, 0.1,0.3]])
print(ein_2D_array)
print(ein_2D_array.shape)
print()

ein_3D_array_mit_einsen=np.ones((2,3,4), dtype=np.int16)
print(ein_3D_array_mit_einsen)
print(ein_3D_array_mit_einsen.shape)
print()

a=np.arange(15).reshape(3,5)
print(a)

b=np.linspace(0, 2*np.pi, 100)
print(b)
print(np.sin(b))