from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
import random

app = Ursina()

# Terreno generado a partir de una textura de mapa de altura
terrain_from_heightmap_texture = Entity(
    model=Terrain('heightmap_1', skip=8),
    scale=(40, 5, 20),
    texture='heightmap_1'
)

# Función para modificar el terreno basado en valores aleatorios
def input(key):
    if key == 'space':
        terrain_from_list.model.height_values = [[random.uniform(0, 255) for _ in column] for column in terrain_from_list.model.height_values]
        terrain_from_list.model.generate()

# Terreno generado a partir de una lista de valores de altura
hv = terrain_from_heightmap_texture.model.height_values.tolist()
terrain_from_list = Entity(
    model=Terrain(height_values=hv),
    scale=(40, 5, 20),
    texture='heightmap_1',
    x=40
)

# Crear la cámara de editor y el cielo
editor_camera = EditorCamera(rotation_speed=200, panning_speed=200)
Sky()

# Crear un jugador y asignarle el terreno como suelo
player = FirstPersonController(model='sphere', color=color.azure, scale=2, origin_y=-.5)
player.collider = 'mesh'
player.gravity = 0.5
player.ground = terrain_from_list

# Actualizar la función para incluir la rotación de la cámara con las teclas de flecha
def update():
    if held_keys['up arrow']:
        editor_camera.rotation_x -= 1
    if held_keys['down arrow']:
        editor_camera.rotation_x += 1
    if held_keys['left arrow']:
        editor_camera.rotation_y += 1
    if held_keys['right arrow']:
        editor_camera.rotation_y -= 1

    # Movimiento del jugador
    direction = Vec3(
        held_keys['d'] - held_keys['a'],
        0,
        held_keys['w'] - held_keys['s']
    ).normalized()
    player.position += direction * time.dt * 8

app.run()
