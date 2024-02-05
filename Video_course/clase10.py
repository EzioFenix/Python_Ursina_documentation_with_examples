from ursina import *


def update():
    # Si la tecla 'a' es presionada, mueve el cubo 5 unidades a la izquierda
    if held_keys['a']:
        cube.x -= 5 * time.dt
    # Si la tecla 'w' es presionada, mueve el cubo 5 unidades hacia adelante
    if held_keys['w']:
        cube.y += 5 * time.dt
    if held_keys['s']:
        cube.y += 5 * time.dt

app = Ursina()

# Crea un cubo en la escena
cube = Entity(model='cube',texture='brick', color=color.white, scale=(1,1,1))

# Inicia la aplicación
app.run()
