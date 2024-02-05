from ursina import *

app = Ursina()

# Velocidad de movimiento del cubo
movement_speed_x = 0.02
movement_speed_y = 0.02

# Crea un cubo con textura de ladrillos
cube = Entity(model='cube', texture='brick', scale=0.05)

def update():
    global movement_speed_x, movement_speed_y
    
    # Mueve el cubo
    cube.x += movement_speed_x
    cube.y += movement_speed_y
    
    # Obtiene los límites de la ventana desde la perspectiva de la cámara
    camera_bounds = camera.get_screen_bounds()
    left_limit, right_limit = camera_bounds[0], camera_bounds[1]
    bottom_limit, top_limit = camera_bounds[2], camera_bounds[3]
    
    # Cambia la dirección del movimiento en x si el cubo alcanza el límite izquierdo o derecho
    if cube.x < left_limit or cube.x > right_limit:
        movement_speed_x *= -1
    
    # Cambia la dirección del movimiento en y si el cubo alcanza el límite inferior o superior
    if cube.y < bottom_limit or cube.y > top_limit:
        movement_speed_y *= -1

app.run()
