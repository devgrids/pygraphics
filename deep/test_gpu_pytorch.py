import torch
import torch.nn as nn

# Supongamos que tienes un modelo llamado 'mi_modelo'
mi_modelo = ...

# Verifica si CUDA (GPU) está disponible
if torch.cuda.is_available():
    # Imprime la cantidad de GPUs disponibles
    num_gpus = torch.cuda.device_count()
    print(f"Se detectaron {num_gpus} GPU(s).")

    if num_gpus > 1:
        # Crea un modelo DataParallel
        mi_modelo_parallel = nn.DataParallel(mi_modelo)
        
        # Asigna el modelo a todas las GPUs
        mi_modelo_parallel = mi_modelo_parallel.to("cuda")

        # Si deseas especificar qué GPUs utilizar, puedes hacerlo así:
        # mi_modelo_parallel = mi_modelo_parallel.to("cuda:0,1")  # Usará las GPU 0 y 1

        # También puedes especificar la GPU al enviar tensores al modelo
        # tensor_on_gpu = tensor_on_gpu.to("cuda:0")  # Envía el tensor a la GPU 0

    else:
        print("Solo una GPU disponible. Utilizando una sola GPU.")
        # Asigna el modelo a la única GPU disponible
        mi_modelo = mi_modelo.to("cuda")
else:
    print("CUDA no está disponible. Utilizando CPU.")
