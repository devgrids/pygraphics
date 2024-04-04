from pygraphics.engine.core.object import Object
from pygraphics.helpers.class_type import ClassType
from pygraphics.engine.core.core import Core

class Component(Object, ClassType, Core):
    def __init__(self):
        Object.__init__(self) 
        ClassType.set_class(self, Component)

    def start(self, *args, **kwargs):
        pass
 
    def update(self, *args, **kwargs):
        pass

    def render(self, *args, **kwargs):
        pass
