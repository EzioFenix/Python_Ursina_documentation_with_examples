from ursina import *

app = Ursina()

# Constante para la velocidad de cambio de escala
SCALE_SPEED = 0.1

cube = Entity(model='cube', texture='brick', scale=(1,1,1))

def update():
    # Aumenta la escala en el eje x con 'a'
    if held_keys['a']:
        cube.scale_x += SCALE_SPEED * time.dt
    # Aumenta la escala en el eje y con 's'
    if held_keys['s']:
        cube.scale_y += SCALE_SPEED * time.dt
    # Aumenta la escala en el eje z con 'w'
    if held_keys['w']:
        cube.scale_z += SCALE_SPEED * time.dt

app.run()
