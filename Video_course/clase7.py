from ursina import Ursina, Entity, color, held_keys, Cylinder, EditorCamera

def update():
    # Controlar la rotación con las flechas del teclado
    if held_keys['up arrow']:
        ed.rotation_x += 1  # Rotar hacia arriba en el eje X
    if held_keys['down arrow']:
        ed.rotation_x -= 1  # Rotar hacia abajo en el eje X
    if held_keys['left arrow']:
        ed.rotation_y += 1  # Rotar a la izquierda en el eje Y
    if held_keys['right arrow']:
        ed.rotation_y -= 1  # Rotar a la derecha en el eje Y

app = Ursina()

# Crear un cilindro
cilindro = Entity(model=Cylinder(resolution=6, start=-.5), color=color.color(60,1,1,.3))

# Crear un marcador de origen para referencia
origin = Entity(model='quad', color=color.orange, scale=(5, .05))

# Usar la cámara de editor para una mejor visualización y control
ed = EditorCamera(rotation_speed=200, panning_speed=200)

app.run()
