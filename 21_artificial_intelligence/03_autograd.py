import torch
x = torch.tensor([[1,2,3],[4,5,6]], dtype=torch.float, requires_grad=True)
f = x.pow(2).sum()#f ist Funktionswert, Quadratsumme
print(f) # tensor(91., grad_fn=<SumBackward0>)
f.backward()
print(x.grad) # df/dx = 2x