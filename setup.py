from setuptools import setup, find_packages

setup(
    name='pygraphics',
    version='0.1',
    description='Python library designed to facilitate graphics manipulation and rendering tasks in various applications',
    author='Yordy Leonidas MV',
    author_email='yordy.lmv.2000@gmail.com',
    packages=find_packages(),
    install_requires=[
        'PyOpenGL',
        'PyOpenGL_accelerate',
        'Pillow',
        'glfw',
        'imgui',
        'spdlog',
        'PyGLM',
        'opencv-python'
    ],
)
