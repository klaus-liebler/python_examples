def f(x):
    return x*x+2*x+4

x_lower=0
x_step=0.01
x_upper_exclusive=10

integral_value=0
x= x_lower
while x<x_upper_exclusive:
    integral_value+=(f(x)*x_step)
    x+=x_step

print("Der Wert des Integrals zwischen", x_lower, "und", x_upper_exclusive, "ist", integral_value)