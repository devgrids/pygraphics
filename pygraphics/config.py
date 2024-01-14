from pygraphics.api.type.render_type import RenderType
from pygraphics.api.type.input_type import InputType
from pygraphics.api.type.gui_type import GuiType

from pygraphics.graphics_api import GraphicsApi
from pygraphics.system import System

import glm
import random

def init():
    GraphicsApi.set_type_graphic(RenderType.GL4)
    GraphicsApi.set_type_input(InputType.GLFW)
    GraphicsApi.set_type_gui(GuiType.IMGUI)
    System.init()

init()
