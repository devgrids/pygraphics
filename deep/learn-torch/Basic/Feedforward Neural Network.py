"""
Un recorrido simple sobre cómo codificar una red neuronal completamente conectada
utilizando la biblioteca PyTorch. Para la demostración, la entrenamos en el conjunto
de datos MNIST, que es muy común y contiene dígitos escritos a mano. En este código,
exploramos cómo crear la red, inicializar una función de pérdida, optimizador,
verificar la precisión y más.

Programado por Aladdin Persson
* 2020-04-08: Codificación inicial
* 2021-03-24: Se agregaron comentarios más detallados y se eliminó parte de
              check_accuracy que solo funcionaría específicamente en MNIST.
* 2022-09-23: Actualizado con comentarios más detallados, docstrings para funciones y
              se verificó que el código todavía funcione según lo previsto.
"""

# Importaciones
import torch
import torch.nn.functional as F  # Funciones sin parámetros, como algunas funciones de activación
import torchvision.datasets as datasets  # Conjuntos de datos estándar
import torchvision.transforms as transforms  # Transformaciones que podemos aplicar a nuestro conjunto de datos para la ampliación
from torch import optim  # Para optimizadores como SGD, Adam, etc.
from torch import nn  # Todos los módulos de redes neuronales
from torch.utils.data import (
    DataLoader,
)  # Facilita la gestión del conjunto de datos al crear mini lotes, etc.
from tqdm import tqdm  # ¡Para una barra de progreso agradable!

# Aquí creamos nuestra red neuronal simple. Para más detalles, aquí estamos subclaseando e
# heredando de nn.Module, esta es la forma más general de crear tus redes y
# permite más flexibilidad. Te animo también a echar un vistazo a nn.Sequential que
# sería más fácil de usar en este escenario, pero quería mostrarte algo que
# "siempre" funciona y es un enfoque general.
class NN(nn.Module):
    def __init__(self, input_size, num_classes):
        """
        Aquí definimos las capas de la red. Creamos dos capas completamente conectadas.

        Parámetros:
            input_size: el tamaño de la entrada, en este caso 784 (28x28)
            num_classes: el número de clases que queremos predecir, en este caso 10 (0-9)

        """
        super(NN, self).__init__()
        # Nuestra primera capa lineal toma input_size, en este caso 784 nodos a 50
        # y nuestra segunda capa lineal lleva 50 a las num_classes que tenemos, en
        # este caso 10.
        self.fc1 = nn.Linear(input_size, 50)
        self.fc2 = nn.Linear(50, num_classes)

    def forward(self, x):
        """
        Aquí, x son las imágenes de MNIST y las pasamos por fc1, fc2 que creamos anteriormente.
        También agregamos una función de activación ReLU entre ellas y para eso (ya que no tiene parámetros)
        recomiendo usar nn.functional (F)

        Parámetros:
            x: imágenes de MNIST

        Devoluciones:
            out: la salida de la red
        """

        x = F.relu(self.fc1(x))
        x = self.fc2(x)
        return x


# Configuramos el dispositivo como cuda para la GPU si está disponible; de lo contrario, se ejecuta en la CPU
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Hiperparámetros
input_size = 784
num_classes = 10
learning_rate = 0.001
batch_size = 64
num_epochs = 10

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
model = NN(input_size=input_size, num_classes=num_classes).to(device)

# Pérdida y optimizador
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=learning_rate)

# Entrenar la red
for epoch in range(num_epochs):
    for batch_idx, (data, targets) in enumerate(tqdm(train_loader)):
        # Llevar los datos a cuda si es posible
        data = data.to(device=device)
        targets = targets.to(device=device)

        # Darle la forma correcta
        data = data.reshape(data.shape[0], -1)

        # Hacia adelante
        scores = model(data)
        loss = criterion(scores, targets)

        # Hacia atrás
        optimizer.zero_grad()
        loss.backward()

        # Paso de descenso de gradiente o Adam
        optimizer.step()


# Verificar la precisión en entrenamiento y prueba para ver qué tan bueno es nuestro modelo
def check_accuracy(loader, model):
    """
    Verifica la precisión de nuestro modelo entrenado dado un cargador y un modelo

    Parámetros:
        loader: torch.utils.data.DataLoader
            Un cargador para el conjunto de datos en el que deseas verificar la precisión
        model: nn.Module
            El modelo del cual deseas verificar la precisión

    Devoluciones:
        acc: flotante
            La precisión del modelo en el conjunto de datos dado por el cargador
    """

    num_correct = 0
    num_samples = 0
    model.eval()

    # No necesitamos realizar un seguimiento de los gradientes aquí, así que lo envolvemos en torch.no_grad()
    with torch.no_grad():
        # Iterar a través de los datos
        for x, y in loader:

            # Mover datos al dispositivo
            x = x.to(device=device)
            y = y.to(device=device)

            # Darle la forma correcta
            x = x.reshape(x.shape[0], -1)

            # Paso hacia adelante
            scores = model(x)
            _, predictions = scores.max(1)

            # Verificar cuántos obtuvimos correctamente
            num_correct += (predictions == y).sum()

            # Realizar un seguimiento del número de muestras
            num_samples += predictions.size(0)

    model.train()
    return num_correct / num_samples


# Verificar la precisión en entrenamiento y prueba para ver qué tan bueno es nuestro modelo
print(f"Precisión en el conjunto de entrenamiento: {check_accuracy(train_loader, model)*100:.2f}")
print(f"Precisión en el conjunto de prueba: {check_accuracy(test_loader, model)*100:.2f}")
