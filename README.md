### PyGraphics: Biblioteca Gráfica para Python con OpenGL

PyGraphics es una biblioteca gráfica desarrollada en Python que utiliza OpenGL para renderizar gráficos en 2D y 3D de manera eficiente. Esta biblioteca está diseñada para facilitar el desarrollo de aplicaciones y juegos interactivos con una interfaz de usuario intuitiva y un rendimiento excepcional. Con PyGraphics, puedes crear ventanas personalizadas, diseñar interfaces de usuario, integrar sprites y mucho más con facilidad.

---

#### Características Principales

- **Renderización en tiempo real:** PyGraphics utiliza OpenGL para renderizar gráficos de forma rápida y eficiente, garantizando un rendimiento óptimo incluso en aplicaciones gráficamente intensivas.

- **Interfaz de Usuario Personalizable:** Crea interfaces de usuario altamente personalizables con la API de PyGraphics, que incluye widgets y herramientas para la gestión de eventos.

- **Sprites y Animaciones:** Integra fácilmente sprites y animaciones en tus aplicaciones y juegos para agregar dinamismo y vida a tus proyectos.

- **Soporte Multiplataforma:** Desarrolla aplicaciones que se ejecuten en múltiples plataformas, incluyendo Windows, macOS y Linux, gracias a la compatibilidad de PyGraphics con Python y OpenGL.

---

#### Instalación

Para instalar PyGraphics, simplemente ejecuta el siguiente comando en tu terminal:

```bash
pip install pygraphics
```

Asegúrate de tener Python y OpenGL instalados en tu sistema antes de proceder con la instalación.

---

#### Ejemplo de Uso

```python
from config import *
from pygraphics.config import *

CAMERA_BOUNDS = (0, 30, 0, 30)

def main(): 

    System.camera.set_projection_matrix(*CAMERA_BOUNDS)

    obj = System.new_object_2d("assets/images/model.jpg")
    obj.transform.position = glm.vec3(15, 15, 0)
    obj.transform.scale = glm.vec3(20, 20, 0)

    def handle():
        System.gui.text("GUI", "Hola Mundo!")

    System.loop(handle)

if __name__ == "__main__":
    main()

```

---

#### Contribución

¡Tu contribución es bienvenida! Si encuentras algún problema o tienes alguna sugerencia para mejorar PyGraphics, no dudes en abrir un issue en nuestro repositorio de GitHub.

[Repositorio de GitHub](https://github.com/devgrids/pygraphics)

---

#### Licencia

PyGraphics se distribuye bajo la licencia MIT, lo que significa que puedes usarla en proyectos comerciales y de código abierto sin restricciones.

---

¡Esperamos que disfrutes utilizando PyGraphics para tus proyectos gráficos en Python! Si tienes alguna pregunta o necesitas ayuda, no dudes en ponerte en contacto con nosotros en nuestro canal de Discord o a través de nuestro correo electrónico de soporte.

¡Gracias por elegir PyGraphics!
