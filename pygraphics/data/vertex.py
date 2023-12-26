import glm

class Vertex:
    def __init__(self, position=None):
        self.position = position if position is not None else glm.vec4(0.0, 0.0, 0.0, 0.0)

print(dir(glm))  # Esto imprimirá todas las funciones y clases disponibles en glm


# Ejemplo de uso
vertex_instance = Vertex(glm.vec4(1.0, 2.0, 3.0, 1.0))
