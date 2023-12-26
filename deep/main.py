import sys
sys.path.append('C:\\dev\\deep')

from pygraphics.Type.RenderType import RenderType
from pygraphics.FactoryEngine import FactoryEngine
from pygraphics.System import System
from pygraphics.Render.GL4Render import GL4Render

def main():
    FactoryEngine.set_type_graphic(RenderType.GL4)
    System.init_system()
    System.main_loop()
    return 0

if __name__ == "__main__":
    main()

