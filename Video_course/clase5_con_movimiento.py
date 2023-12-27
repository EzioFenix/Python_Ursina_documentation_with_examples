from ursina import *

def update():
    # Rotar en el eje Y (izquierda / derecha)
    if held_keys['left arrow']:
        grid.rotation_y += time.dt * 100
    if held_keys['right arrow']:
        grid.rotation_y -= time.dt * 100

    # Rotar en el eje X (arriba / abajo)
    if held_keys['up arrow']:
        grid.rotation_x += time.dt * 100
    if held_keys['down arrow']:
        grid.rotation_x -= time.dt * 100

app = Ursina()

# Crear un grid
grid = Entity()

# Crear cuadrados en el grid y asignarles colores aleatorios
for y in range(5):
    for x in range(5):
        b = Button(parent=grid, position=(x, y), color=color.random_color())

# Asegurarse de que la cámara no rota con el grid
camera.parent = scene

app.run()
