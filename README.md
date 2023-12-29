----------------------------------------------------------------

Crea un entorno virtual (si no lo has hecho): python -m venv env
o python3.11 -m venv env

Ver versión de Python: python --version

Activa el entorno virtual:

En PowerShell: .\env\Scripts\Activate
En la terminal de comandos: .\env\Scripts\activate.bat

Ejecutar: python main.py
Desactivar: deactivate

----------------------------------------------------------------

Instalar pygraphics:

pip uninstall pygraphics
pip install -e ./pygraphics

----------------------------------------------------------------

Instalar librerias:

pip install PyOpenGL PyOpenGL_accelerate Pillow
pip install glfw
#pip install imgui[glfw] || pip install imgui==<version>[glfw]
pip install imgui
pip install spdlog
pip install PyGLM
pip install numpy
pip install torch
pip install pandas
pip install matplotlib

NOT RECOMEND: pip install git+https://github.com/swistakm/pyimgui.git
pip install git+https://github.com/swistakm/pyimgui.git@<tag-branch-or-commit>

----------------------------------------------------------------