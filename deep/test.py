import glfw
from OpenGL.GL import *
import numpy as np

def draw_guizmo():
    # Ejes X, Y, Z
    glBegin(GL_LINES)
    
    # Eje X en rojo
    glColor3f(1, 0, 0)
    glVertex3f(0, 0, 0)
    glVertex3f(1, 0, 0)

    # Eje Y en verde
    glColor3f(0, 1, 0)
    glVertex3f(0, 0, 0)
    glVertex3f(0, 1, 0)

    # Eje Z en azul
    glColor3f(0, 0, 1)
    glVertex3f(0, 0, 0)
    glVertex3f(0, 0, 1)

    glEnd()

def main():
    if not glfw.init():
        return

    window = glfw.create_window(800, 600, "3D Guizmo Example", None, None)
    if not window:
        glfw.terminate()
        return

    glfw.make_context_current(window)
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glEnable(GL_DEPTH_TEST)

    while not glfw.window_should_close(window):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        # Aquí ajustas la cámara/proyección si lo necesitas
        # ...

        draw_guizmo()

        glfw.swap_buffers(window)
        glfw.poll_events()

    glfw.terminate()

if __name__ == "__main__":
    main()
