import torch
import matplotlib.pyplot as plt
from PIL import Image
import torch 
from torchvision import transforms
from torchvision import models
from torchvision.models.alexnet import AlexNet_Weights

img = Image.open('bild2.jpg')
plt.imshow(img)
plt.show()

transform = transforms.Compose([
    transforms.Resize(256),
    transforms.CenterCrop(224),  
    transforms.ToTensor(),
    transforms.Normalize(
        mean=[0.485, 0.456, 0.406],
        std=[0.229, 0.224, 0.225])])
img_tensor = transform(img)
batch = img_tensor.unsqueeze(0)
model = models.alexnet(weights=AlexNet_Weights.DEFAULT)
device = "cuda" if torch.cuda.is_available() else "cpu"
model.eval()
model.to(device)
y = model(batch.to(device))
y_max, index = torch.max(y,1)

print(type(img_tensor), img_tensor.shape)
print(batch.shape)# out: torch.Size([1, 3, 224, 224])
print("The AI-Device is", device)
print(y.shape)# out: torch.Size([1, 1000])
print(index, y_max)
with open('imagenet_class_labels.txt') as f:
    classes = [line.strip() for line in f.readlines()]
print(classes[index])