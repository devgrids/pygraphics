import cv2
import numpy as np
import glfw
from OpenGL.GL import *
from OpenGL.GL.shaders import compileProgram, compileShader

# Código del shader de vértices
vertex_src = """
# version 330
layout(location = 0) in vec3 a_position;
layout(location = 1) in vec2 a_texture;
out vec2 v_texture;
void main()
{
    gl_Position = vec4(a_position, 1.0);
    v_texture = a_texture;
}
"""

# Código del shader de fragmentos
fragment_src = """
# version 330
in vec2 v_texture;
out vec4 out_color;
uniform sampler2D s_texture;
void main()
{
    out_color = texture(s_texture, v_texture);
}
"""

# Inicializar GLFW
if not glfw.init():
    raise Exception("GLFW no se puede inicializar")

# Configuración de la ventana
glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR, 3)
glfw.window_hint(glfw.CONTEXT_VERSION_MINOR, 3)
glfw.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE)
glfw.window_hint(glfw.OPENGL_FORWARD_COMPAT, GL_TRUE)

# Crear ventana
window = glfw.create_window(1280, 720, "GLFW OpenCV Video Player", None, None)

if not window:
    glfw.terminate()
    raise Exception("La ventana GLFW no se pudo crear")

glfw.make_context_current(window)

# Compilar el programa de shaders
shader = compileProgram(compileShader(vertex_src, GL_VERTEX_SHADER), compileShader(fragment_src, GL_FRAGMENT_SHADER))

# Definir los vértices y las coordenadas de textura
vertices = [-1, -1, 0, 0, 0,
            1, -1, 0, 1, 0,
            1,  1, 0, 1, 1,
           -1,  1, 0, 0, 1]

vertices = np.array(vertices, dtype=np.float32)

# Crear VBO y VAO
VBO = glGenBuffers(1)
VAO = glGenVertexArrays(1)
glBindVertexArray(VAO)
glBindBuffer(GL_ARRAY_BUFFER, VBO)
glBufferData(GL_ARRAY_BUFFER, vertices.nbytes, vertices, GL_STATIC_DRAW)

# Posición
glEnableVertexAttribArray(0)
glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 20, ctypes.c_void_p(0))

# Textura
glEnableVertexAttribArray(1)
glVertexAttribPointer(1, 2, GL_FLOAT, GL_FALSE, 20, ctypes.c_void_p(12))

# Crear textura
texture = glGenTextures(1)
glBindTexture(GL_TEXTURE_2D, texture)
glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)

# Cargar video
cap = cv2.VideoCapture("deep/assets/sex.mp4")

while not glfw.window_should_close(window):
    glfw.poll_events()

    ret, frame = cap.read()
    if not ret:
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)  # Vuelve al inicio del video
        continue

    frame = cv2.flip(frame, 0)  # Vertical flip
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    h, w, _ = frame.shape

    # Enviar el frame a la textura
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, w, h, 0, GL_RGB, GL_UNSIGNED_BYTE, frame)

    glClear(GL_COLOR_BUFFER_BIT)
    glUseProgram(shader)
    glBindVertexArray(VAO)
    glDrawArrays(GL_TRIANGLE_FAN, 0, 4)
    glfw.swap_buffers(window)

# Limpieza
cap.release()
glDeleteVertexArrays(1, [VAO])
glDeleteBuffers(1, [VBO])
glDeleteProgram(shader)
glfw.terminate()
