# Importando las bibliotecas necesarias
import torch
import torch.nn as nn
import torch.optim as optim
from torchvision import datasets, transforms
from torch.utils.data import DataLoader
import os

# Imprimiendo la versión de PyTorch
print(torch.__version__)

# Definición de la transformación para el conjunto de entrenamiento
train_transform = transforms.Compose([
    transforms.RandomResizedCrop(64),       # Corta y redimensiona las imágenes
    transforms.RandomHorizontalFlip(),      # Voltea horizontalmente algunas imágenes aleatoriamente
    transforms.ToTensor(),                   # Convierte las imágenes en tensores
    transforms.Normalize(mean=[0.5, 0.5, 0.5], std=[0.5, 0.5, 0.5])  # Normaliza los tensores
])

# Creación del conjunto de entrenamiento
training_set = datasets.ImageFolder(root='deep/dataset/training_set', transform=train_transform)
train_loader = DataLoader(dataset=training_set, batch_size=32, shuffle=True)

# Definición de la transformación para el conjunto de prueba
test_transform = transforms.Compose([
    transforms.Resize((64, 64)),              # Redimensiona las imágenes
    transforms.ToTensor(),                    # Convierte las imágenes en tensores
    transforms.Normalize(mean=[0.5, 0.5, 0.5], std=[0.5, 0.5, 0.5])  # Normaliza los tensores
])

# Creación del conjunto de prueba
test_set = datasets.ImageFolder(root='deep/dataset/test_set', transform=test_transform)
test_loader = DataLoader(dataset=test_set, batch_size=32, shuffle=False)

# Definición de la arquitectura de la red neuronal convolucional (CNN)
class CNN(nn.Module):
    def __init__(self):
        super(CNN, self).__init__()
        # Definición de las capas de la red
        self.conv1 = nn.Conv2d(3, 32, kernel_size=3, stride=1, padding=1)
        self.pool = nn.MaxPool2d(kernel_size=2, stride=2)
        self.conv2 = nn.Conv2d(32, 32, kernel_size=3, stride=1, padding=1)
        self.fc1 = nn.Linear(32 * 16 * 16, 128)
        self.fc2 = nn.Linear(128, 1)
        self.sigmoid = nn.Sigmoid()

    def forward(self, x):
        # Definición de cómo se propagan los datos a través de la red
        x = self.pool(nn.functional.relu(self.conv1(x)))
        x = self.pool(nn.functional.relu(self.conv2(x)))
        x = x.view(-1, 32 * 16 * 16)
        x = nn.functional.relu(self.fc1(x))
        x = self.sigmoid(self.fc2(x))
        return x

# Inicialización de la CNN
cnn = CNN()

# Definición de la función de pérdida y el optimizador
criterion = nn.BCELoss()
optimizer = optim.Adam(cnn.parameters(), lr=0.001)

# Mover el modelo a la GPU si está disponible
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
cnn.to(device)

# Entrenamiento de la CNN
num_epochs = 25
for epoch in range(num_epochs):
    print(f'Epoch {epoch + 1}/{num_epochs}')
    for images, labels in train_loader:
        images, labels = images.to(device), labels.to(device)
        optimizer.zero_grad()
        outputs = cnn(images)
        loss = criterion(outputs, labels.float().view(-1, 1))
        loss.backward()
        optimizer.step()

# Preparación de una sola predicción
import numpy as np
from PIL import Image
from torchvision import transforms

# Cargar y preprocesar la imagen de prueba
test_image_path = 'deep/dataset/single_prediction/cat.png'
test_image = Image.open(test_image_path)
test_transform = transforms.Compose([
    transforms.Resize((64, 64)),
    transforms.ToTensor(),
    lambda x: x[:3, :, :],  # Descartar el canal alfa si existe
    transforms.Normalize(mean=[0.5, 0.5, 0.5], std=[0.5, 0.5, 0.5])
])
test_image = test_transform(test_image)

# Mover la imagen de prueba a la GPU si está disponible
test_image = test_image.to(device)

# Realizar la predicción
with torch.no_grad():
    cnn.eval()
    result = cnn(test_image.unsqueeze(0))  # Mantén unsqueeze(0) aquí si es necesario
    prediction = 'dog' if result.item() > 0.5 else 'cat'
    print(f'Predicción: {prediction}')

# Guardar los pesos de la CNN
torch.save(cnn.state_dict(), 'deep/cat_or_dog_predict.pth')
