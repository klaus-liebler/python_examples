import torch
import math
device = "cuda" if torch.cuda.is_available() else "cpu"
x = torch.tensor([[1,2,3],[4,5,6]], device=device)
y = torch.tensor([[7,8,9],[10,11,12]], device=device)
z = x + y
print("Result", z, "\nSize  ", z.size(), "\nDevice", z.device)

alpha= torch.linspace(0,200,101)
print(alpha)

beta = torch.rand(50)
print(beta)

x = torch.tensor([[1,2],[3,4],[5,6],[7,8],[9,10]])
gamma = x[0:5:2,1] # [start:end:step]
print(gamma)
gamma =x.t()
print(gamma)

A=torch.tensor([[0.25*math.pi, 0.5*math.pi],[0.75*math.pi, 1.0*math.pi]])
print(A.sin())

beta = torch.rand(100000)
print(beta.mean())