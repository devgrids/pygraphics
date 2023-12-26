# entrenar_modelo.py

import torch
import torch.nn as nn
import torch.optim as optim

# Paso 1: Definir cómo se ve nuestra "máquina"
class CelsiusToFahrenheit(nn.Module):
    def __init__(self):
        super(CelsiusToFahrenheit, self).__init__()
        # Nuestra máquina tiene una parte (llamada 'linear') que aprende la conversión
        self.linear = nn.Linear(1, 1)

    def forward(self, x):
        # Aquí decimos cómo usar esa parte para hacer la conversión
        return self.linear(x)

# Paso 2: Crear una máquina nueva usando la definición de arriba
modelo = CelsiusToFahrenheit()

# Paso 3: Darle ejemplos a la máquina para que aprenda
# Estos son temperaturas en Celsius y sus equivalentes en Fahrenheit
celsius = torch.tensor([[-40], [-10], [0], [8], [15], [22], [38]], dtype=torch.float32)
fahrenheit = torch.tensor([[-40], [14], [32], [46], [59], [72], [100]], dtype=torch.float32)

# Paso 4: Preparar las herramientas que la máquina usará para aprender
# 'criterio' es cómo la máquina verifica si sus respuestas son buenas
criterio = nn.MSELoss()
# 'optimizador' es cómo la máquina mejora sus respuestas
optimizador = optim.SGD(modelo.parameters(), lr=0.001)

# Paso 5: Entrenar a la máquina con los ejemplos
for epoch in range(1000):
    # La máquina intenta convertir las temperaturas
    predicciones = modelo(celsius)
    # Comprobamos qué tan buenas son sus respuestas
    perdida = criterio(predicciones, fahrenheit)

    # Decimos a la máquina cómo mejorar
    optimizador.zero_grad()
    perdida.backward()
    optimizador.step()

    # Imprimimos cómo va mejorando
    if epoch % 100 == 99:
        print(f'Época {epoch+1}, Pérdida: {perdida.item()}')

# Paso 6: Guardar la máquina entrenada para usarla después
torch.save(modelo.state_dict(), 'mi_modelo_entrenado.pth')
