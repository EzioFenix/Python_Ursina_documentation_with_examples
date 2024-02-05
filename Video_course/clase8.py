from ursina import Ursina, Entity, Circle, Pipe, color, EditorCamera, held_keys

def update():
    # Controlar la rotación con las flechas del teclado
    if held_keys['up arrow']:
        editor_camera.rotation_x += 1
    if held_keys['down arrow']:
        editor_camera.rotation_x -= 1
    if held_keys['left arrow']:
        editor_camera.rotation_y += 1
    if held_keys['right arrow']:
        editor_camera.rotation_y -= 1

app = Ursina()

# Generar un camino (path) utilizando los vértices de un círculo, escalados por 5
path = [vertex * 5 for vertex in Circle().vertices]

# Añadir el primer punto al final del camino para cerrar el círculo
path.append(path[0])

# Crear una entidad con el modelo de Pipe utilizando el camino generado
pipe_entity = Entity(model=Pipe(path=path, cap_ends=False))

# Imprimir la cantidad de vértices y colores del modelo
print(len(pipe_entity.model.vertices), len(pipe_entity.model.colors))

# Configurar la cámara de editor para una mejor visualización y control
editor_camera = EditorCamera(rotation_speed=200, panning_speed=200)

# Crear una entidad para marcar el origen con un cubo magenta
origin_marker = Entity(model='cube', color=color.magenta)
origin_marker.scale *= .25

app.run()
