# Python_Ursina_documentation_with_examples
Esta documentación esta enfocada a como usar ursina de python, mediante ejemplos y explicaciones, complementado esta manera la documentación oficial.

# Clase 0: ¿Qué es ursina?

# Clase 1: Tú primer programa

Primero hay que hacer un entorno virtual

```
python -m venv venv
```

activar el entorno:

- **Winwdows: (powershell)**

```
.\venv\Scripts\Activate.ps1
```



Instalamos el motor

```
pip install ursina
```

tambíen hay que instalar para tener sonido (una alternativa, pero no es necesario, ya que ursina tiene para reproducir sonido)

```bash
pip install playsound
```



## Primer programa

```python
from ursina import * # Importa la aplicación del motor 

app = Ursina() # Inicializa tu aplicación Ursina

app.run() # Ejecuta la aplicación

```

El resultado es el siguiente

![](assets/image-20231208102025504.png)

Felicidades haz hecho tu primer programa usando el motor ursina.



# Referencias

Excelente guía rapida:

-  Ursina for dummies , https://www.ursinaengine.org/ursina_for_dummies.html

Una serie (playlist) de videos viejos de como usarlo pero muy funcionales:

- https://www.youtube.com/playlist?list=PLgQYnHnDxgtg-I3m01mGc5wfJwqpT9S3i

