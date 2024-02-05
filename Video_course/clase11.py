from ursina import *

app = Ursina()

# Constante para la velocidad de rotación (grados por pulsación de tecla)
ROTATION_SPEED = 45

cube = Entity(model='cube', texture='brick', scale=(1,1,1))

def update():
    # Rotación en el eje x con 'a'
    if held_keys['a']:
        cube.rotation_x += ROTATION_SPEED * time.dt
    # Rotación en el eje y con 's'
    if held_keys['s']:
        cube.rotation_y += ROTATION_SPEED * time.dt
    # Rotación en el eje z con 'w'
    if held_keys['w']:
        cube.rotation_z += ROTATION_SPEED * time.dt

app.run()
