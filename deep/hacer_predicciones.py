# hacer_predicciones.py

import torch
import torch.nn as nn

# Paso 1: Recordar cómo se ve la "máquina"
class CelsiusToFahrenheit(nn.Module):
    def __init__(self):
        super(CelsiusToFahrenheit, self).__init__()
        # La máquina tiene una parte que aprende la conversión
        self.linear = nn.Linear(1, 1)

    def forward(self, x):
        # Aquí decimos cómo usar esa parte para hacer la conversión
        return self.linear(x)

# Paso 2: Traer de vuelta la máquina que ya aprendió
modelo_cargado = CelsiusToFahrenheit()
modelo_cargado.load_state_dict(torch.load('deep/mi_modelo_entrenado.pth'))
modelo_cargado.eval()  # La preparamos para hacer cálculos

# Paso 3: Hacer cálculos nuevos con la máquina
def predecir_fahrenheit(celsius):
    # Le pedimos a la máquina que convierta la temperatura
    with torch.no_grad():
        return modelo_cargado(torch.tensor([[celsius]], dtype=torch.float32)).item()

# Ejemplo: Convertir 100 grados Celsius a Fahrenheit
celsius = 100
fahrenheit = predecir_fahrenheit(celsius)
print(f"{celsius} grados Celsius son aproximadamente {fahrenheit} grados Fahrenheit.")
