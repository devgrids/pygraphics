from pygraphics.api.gui.gui import Gui
import os
import sys

if os.getenv("XDG_SESSION_TYPE") == "wayland":
    os.environ["XDG_SESSION_TYPE"] = "x11"

import glfw
from OpenGL.GL import *
from OpenGL.GL.shaders import compileProgram, compileShader
import imgui
from imgui.integrations.glfw import GlfwRenderer

active = {
    "window": True,
    "child": False,
    "tooltip": False,
    "menu bar": False,
    "popup": False,
    "popup modal": False,
    "popup context item": False,
    "popup context window": False,
    "drag drop": False,
    "group": False,
    "tab bar": False,
    "list box": False,
    "popup context void": False,
    "table": False,
}
path_to_font = None  # "path/to/font.ttf"
path_to_font = "pygraphics/resources/fonts/norwester.otf"
opened_state = True

class GlGlfwImgui(Gui):
    def __init__(self):
        self.__render = None
        self.window = None
        self.impl = None
        self.font = None
        self.flag = False
        self.change_swap_interval = False

    # def __del__(self):
    #     self.clear()

    def init(self):
        imgui.create_context()
        io = imgui.get_io()
        self.font = io.fonts.add_font_from_file_ttf(path_to_font, 30) if path_to_font is not None else None

    def update(self):
        imgui.new_frame()

    def render(self):
        imgui.render()
        self.impl.render(imgui.get_draw_data())
        self.impl.process_inputs()

    def clear(self):
        self.impl.shutdown()
    
    def link_render(self, render):
        self.__render = render
        self.window = self.__render.get_window()
        self.impl = GlfwRenderer(self.window, True)
        self.impl.refresh_font_texture()

    def frame_commands(self):
        io = imgui.get_io()
        #io.config_flags |= imgui.CONFIG_DOCKING_ENABLE
        #io.config_flags |= imgui.CONFIG_VIEWPORTS_ENABLE

        if io.key_ctrl and io.keys_down[glfw.KEY_Q]:
            sys.exit(0)

        with imgui.begin_main_menu_bar() as main_menu_bar:
            if main_menu_bar.opened:
                with imgui.begin_menu("File", True) as file_menu:
                    if file_menu.opened:
                        clicked_quit, selected_quit = imgui.menu_item("Quit", "Ctrl+Q")
                        if clicked_quit:
                            sys.exit(0)

        # turn examples on/off
        with imgui.begin("Active examples"):
            for label, enabled in active.copy().items():
                _, enabled = imgui.checkbox(label, enabled)
                active[label] = enabled

        if active["window"]:
            with imgui.begin("Hello, Imgui!"):
                imgui.text("Hello, World!")

        if active["child"]:
            with imgui.begin("Example: child region"):
                with imgui.begin_child("region", 150, -50, border=True):
                    imgui.text("inside region")
                imgui.text("outside region")

        if active["tooltip"]:
            with imgui.begin("Example: tooltip"):
                imgui.button("Click me!")
                if imgui.is_item_hovered():
                    with imgui.begin_tooltip():
                        imgui.text("This button is clickable.")

        if active["menu bar"]:
            try:
                flags = imgui.WINDOW_MENU_BAR
                with imgui.begin("Child Window - File Browser", flags=flags):
                    with imgui.begin_menu_bar() as menu_bar:
                        if menu_bar.opened:
                            with imgui.begin_menu('File') as file_menu:
                                if file_menu.opened:
                                    clicked, state = imgui.menu_item('Close')
                                    if clicked:
                                        active["menu bar"] = False
                                        raise Exception
            except Exception:
                print("exception handled")

        if active["popup"]:
            with imgui.begin("Example: simple popup"):
                if imgui.button("select"):
                    imgui.open_popup("select-popup")
                imgui.same_line()
                with imgui.begin_popup("select-popup") as popup:
                    if popup.opened:
                        imgui.text("Select one")
                        imgui.separator()
                        imgui.selectable("One")
                        imgui.selectable("Two")
                        imgui.selectable("Three")

        if active["popup modal"]:
            with imgui.begin("Example: simple popup modal"):
                if imgui.button("Open Modal popup"):
                    imgui.open_popup("select-popup-modal")
                imgui.same_line()
                with imgui.begin_popup_modal("select-popup-modal") as popup:
                    if popup.opened:
                        imgui.text("Select an option:")
                        imgui.separator()
                        imgui.selectable("One")
                        imgui.selectable("Two")
                        imgui.selectable("Three")

        if active["popup context item"]:
            with imgui.begin("Example: popup context view"):
                imgui.text("Right-click to set value.")
                with imgui.begin_popup_context_item("Item Context Menu") as popup:
                    if popup.opened:
                        imgui.selectable("Set to Zero")

        if active["popup context window"]:
            with imgui.begin("Example: popup context window"):
                with imgui.begin_popup_context_window() as popup:
                    if popup.opened:
                        imgui.selectable("Clear")

        if active["popup context void"]:
            with imgui.begin_popup_context_void() as popup:
                if popup.opened:
                    imgui.selectable("Clear")

        if active["drag drop"]:
            with imgui.begin("Example: drag and drop"):
                imgui.button('source')
                with imgui.begin_drag_drop_source() as src:
                    if src.dragging:
                        imgui.set_drag_drop_payload('itemtype', b'payload')
                        imgui.button('dragged source')
                imgui.button('dest')
                with imgui.begin_drag_drop_target() as dst:
                    if dst.hovered:
                        payload = imgui.accept_drag_drop_payload('itemtype')
                        if payload is not None:
                            print('Received:', payload)

        if active["group"]:
            with imgui.begin("Example: item groups"):
                with imgui.begin_group():
                    imgui.text("First group (buttons):")
                    imgui.button("Button A")
                    imgui.button("Button B")
                imgui.same_line(spacing=50)
                with imgui.begin_group():
                    imgui.text("Second group (text and bullet texts):")
                    imgui.bullet_text("Bullet A")
                    imgui.bullet_text("Bullet B")

        if active["tab bar"]:
            with imgui.begin("Example Tab Bar"):
                with imgui.begin_tab_bar("MyTabBar") as tab_bar:
                    if tab_bar.opened:
                        with imgui.begin_tab_item("Item 1") as item1:
                            if item1.opened:
                                imgui.text("Here is the tab content!")
                        with imgui.begin_tab_item("Item 2") as item2:
                            if item2.opened:
                                imgui.text("Another content...")
                        global opened_state
                        with imgui.begin_tab_item("Item 3", opened=opened_state) as item3:
                            opened_state = item3.opened
                            if item3.selected:
                                imgui.text("Hello Saylor!")

        if active["list box"]:
            with imgui.begin("Example: custom listbox"):
                with imgui.begin_list_box("List", 200, 100) as list_box:
                    if list_box.opened:
                        imgui.selectable("Selected", True)
                        imgui.selectable("Not Selected", False)

        if active["table"]:
            with imgui.begin("Example: table"):
                with imgui.begin_table("data", 2) as table:
                    if table.opened:
                        imgui.table_next_column()
                        imgui.table_header("A")
                        imgui.table_next_column()
                        imgui.table_header("B")

                        imgui.table_next_row()
                        imgui.table_next_column()
                        imgui.text("123")

                        imgui.table_next_column()
                        imgui.text("456")

                        imgui.table_next_row()
                        imgui.table_next_column()
                        imgui.text("789")

                        imgui.table_next_column()
                        imgui.text("111")

                        imgui.table_next_row()
                        imgui.table_next_column()
                        imgui.text("222")

                        imgui.table_next_column()
                        imgui.text("333") 

    def demo(self):
        if self.font is not None:
            imgui.push_font(self.font)
        self.frame_commands()
        if imgui.tree_node("tree_node"):
            imgui.text("tree_node")
            imgui.tree_pop()
        if self.font is not None:
            imgui.pop_font()

    def widget(self, id, code=None):
        self.flag = False
        with imgui.begin(id):
            if code is not None:
                code()
            
    def text(self, id, text="None"):
        def widget_text():
            imgui.text(text)
        self.widget(id, widget_text)

    def button(self, id: str, label: str) -> bool:
        def widget_button():
            if imgui.button(label):
                self.flag = True
        self.widget(id, widget_button)
        return self.flag

    def set_drag_float_3f(self, id: str, label: str, value, description: str = "") -> bool:
        def widget_drag_float_3f():
            changed, values = imgui.drag_float3(label, value.x, value.y, value.z, 
                                                change_speed=0.1,
                                                min_value=-1000.0, 
                                                max_value=1000.0, 
                                                format="%.3f")
            if changed:
                value.x = values[0]
                value.y = values[1]
                value.z = values[2]
                self.flag = True
        self.widget(id, widget_drag_float_3f)
        return self.flag
    
    def info(self):
        with imgui.begin("Info"):

            io = imgui.get_io()
            imgui.begin_group()

            imgui.new_line()
            imgui.text("Application average %.3f ms/frame (%.1f FPS)" % (1000.0 / io.framerate, io.framerate))
            if imgui.button("Swap Interval"):
                self.change_swap_interval = not self.change_swap_interval
                glfw.swap_interval(1 if self.change_swap_interval else 0)
            imgui.new_line()

            with imgui.begin_tab_bar("TabBar") as tab_bar:
                if tab_bar.opened:
                    with imgui.begin_tab_item("Display") as item1:
                        if item1.selected:
                            imgui.text("OpenGL V.%s" % glGetString(GL_VERSION).decode('utf-8'))
                            imgui.text("GLSL V.%s" % glGetString(GL_SHADING_LANGUAGE_VERSION).decode('utf-8'))
                            imgui.text("Vendor: %s" % glGetString(GL_VENDOR).decode('utf-8'))
                            imgui.text("Gpu: %s" % glGetString(GL_RENDERER).decode('utf-8'))
                            imgui.text("Fps: %.1f" % io.framerate)
                            imgui.text("Average: %.2f ms/frame" % (1000.0 / io.framerate))
                    global opened_state
                    with imgui.begin_tab_item("Author", opened=opened_state) as item3:
                        opened_state = item3.opened
                        if item3.selected:
                            imgui.text("By Yordy Leonidas Moreno Vasquez")
                        
            imgui.end_group()
                        
            
                
            


            

    

        


# import imgui
# help(imgui.collapsing_header)
