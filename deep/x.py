import imgui
from imgui.integrations.glfw import GlfwRenderer
import glfw
from tkinter import Tk, filedialog
from PIL import Image
import numpy as np
from OpenGL.GL import *

class ImGuiFileDialog:
    def __init__(self):
        self.file_path = None
        self.show_dialog = False

    def render(self):
        imgui.text("Seleccione una imagen:")
        imgui.same_line()
        if imgui.button("Abrir"):
            self.show_dialog = True

        if self.show_dialog:
            root = Tk()
            root.withdraw()  # Oculta la ventana principal de Tkinter

            file_path = filedialog.askopenfilename(title="Seleccionar archivo", filetypes=[("Imágenes", "*.png;*.jpg;*.jpeg;*.bmp")])

            if file_path:
                self.file_path = file_path
                self.show_dialog = False

    def get_file_path(self):
        return self.file_path

def load_texture(file_path):
    image = Image.open(file_path)
    img_data = np.array(image.convert("RGBA").tobytes(), dtype=np.uint8)
    width, height = image.size

    texture_id = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, texture_id)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, width, height, 0, GL_RGBA, GL_UNSIGNED_BYTE, img_data)
    glBindTexture(GL_TEXTURE_2D, 0)

    return texture_id, width, height

def main():
    glfw.init()
    glfw.window_hint(glfw.SAMPLES, 4)
    window = glfw.create_window(800, 600, "ImGui File Dialog Example", None, None)
    glfw.make_context_current(window)

    imgui.create_context()
    imgui.get_io().fonts.get_tex_data_as_rgba32()
    renderer = GlfwRenderer(window)

    file_dialog = ImGuiFileDialog()

    while not glfw.window_should_close(window):
        glfw.poll_events()
        imgui.new_frame()

        file_dialog.render()

        if file_dialog.get_file_path():
            texture_id, texture_width, texture_height = load_texture(file_dialog.get_file_path())
            imgui.image(texture_id, width=texture_width, height=texture_height)

        imgui.render()
        renderer.render(imgui.get_draw_data())

        glfw.swap_buffers(window)

    # Mover la destrucción del contexto al final del bucle principal
    # para evitar que se intente destruir el contexto después de cerrar la ventana
    renderer.shutdown()
    imgui.destroy_context()
    glfw.terminate()

if __name__ == "__main__":
    main()
