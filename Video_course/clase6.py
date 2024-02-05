from ursina import Ursina, Entity, color, EditorCamera, Cone, held_keys

def update():
    # Controlar la rotación con las flechas del teclado
    if held_keys['up arrow']:
        cono.rotation_x += 1  # Rotar hacia arriba en el eje X
    if held_keys['down arrow']:
        cono.rotation_x -= 1  # Rotar hacia abajo en el eje X
    if held_keys['left arrow']:
        cono.rotation_y += 1  # Rotar a la izquierda en el eje Y
    if held_keys['right arrow']:
        cono.rotation_y -= 1  # Rotar a la derecha en el eje Y

app = Ursina()

# Crear un cono con más lados para que parezca más redondo
cono = Entity(model=Cone(3), texture='brick', scale=1)

# Crear un marcador de origen para referencia
origin = Entity(model='quad', color=color.orange, scale=(.05, .05))

# Usar la cámara de editor para una mejor visualización y control
ed = EditorCamera()

app.run()
