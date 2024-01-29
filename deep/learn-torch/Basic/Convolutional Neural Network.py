"""
Un recorrido simple de cómo codificar una red neuronal convolucional (CNN)
utilizando la biblioteca PyTorch. Para la demostración, la entrenamos en el muy
común conjunto de datos MNIST de dígitos escritos a mano. En este código, se
explica cómo crear la red, así como inicializar una función de pérdida, un optimizador,
verificar la precisión y más.

Programado por Aladdin Persson
* 2020-04-08: Codificación inicial
* 2021-03-24: Comentarios más detallados y pequeña revisión del código
* 2022-12-19: Pequeña revisión del código, comprobado que funciona con la última versión de PyTorch
"""

# Importaciones
import torch
import torch.nn.functional as F  # Funciones sin parámetros, como algunas funciones de activación
import torchvision.datasets as datasets  # Conjuntos de datos estándar
import torchvision.transforms as transforms  # Transformaciones que podemos realizar en nuestro conjunto de datos para el aumento
from torch import optim  # Para optimizadores como SGD, Adam, etc.
from torch import nn  # Todos los módulos de redes neuronales
from torch.utils.data import (
    DataLoader,
)  # Facilita la gestión del conjunto de datos mediante la creación de mini lotes, etc.
from tqdm import tqdm  # ¡Para una barra de progreso agradable!

# CNN simple
class CNN(nn.Module):
    def __init__(self, in_channels=1, num_classes=10):
        super(CNN, self).__init__()
        self.conv1 = nn.Conv2d(
            in_channels=in_channels,
            out_channels=8,
            kernel_size=3,
            stride=1,
            padding=1,
        )
        self.pool = nn.MaxPool2d(kernel_size=2, stride=2)
        self.conv2 = nn.Conv2d(
            in_channels=8,
            out_channels=16,
            kernel_size=3,
            stride=1,
            padding=1,
        )
        self.fc1 = nn.Linear(16 * 7 * 7, num_classes)

    def forward(self, x):
        x = F.relu(self.conv1(x))
        x = self.pool(x)
        x = F.relu(self.conv2(x))
        x = self.pool(x)
        x = x.reshape(x.shape[0], -1)
        x = self.fc1(x)
        return x


# Establecer dispositivo
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Hiperparámetros
in_channels = 1
num_classes = 10
learning_rate = 3e-4  # Constante de Karpathy
batch_size = 64
num_epochs = 3

# Cargar datos
train_dataset = datasets.MNIST(
    root="dataset/", train=True, transform=transforms.ToTensor(), download=True
)
test_dataset = datasets.MNIST(
    root="dataset/", train=False, transform=transforms.ToTensor(), download=True
)
train_loader = DataLoader(dataset=train_dataset, batch_size=batch_size, shuffle=True)
test_loader = DataLoader(dataset=test_dataset, batch_size=batch_size, shuffle=True)

# Inicializar la red
model = CNN(in_channels=in_channels, num_classes=num_classes).to(device)

# Pérdida y optimizador
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=learning_rate)

# Entrenar la red
for epoch in range(num_epochs):
    for batch_idx, (data, targets) in enumerate(tqdm(train_loader)):
        # Obtener datos en cuda si es posible
        data = data.to(device=device)
        targets = targets.to(device=device)

        # forward
        scores = model(data)
        loss = criterion(scores, targets)

        # backward
        optimizer.zero_grad()
        loss.backward()

        # descenso de gradiente o paso de adam
        optimizer.step()

# Verificar precisión en entrenamiento y prueba para ver qué tan buena es nuestra red
def check_accuracy(loader, model):
    num_correct = 0
    num_samples = 0
    model.eval()

    with torch.no_grad():
        for x, y in loader:
            x = x.to(device=device)
            y = y.to(device=device)

            scores = model(x)
            _, predictions = scores.max(1)
            num_correct += (predictions == y).sum()
            num_samples += predictions.size(0)

    model.train()
    return num_correct / num_samples


print(f"Precisión en el conjunto de entrenamiento: {check_accuracy(train_loader, model)*100:.2f}")
print(f"Precisión en el conjunto de prueba: {check_accuracy(test_loader, model)*100:.2f}")
