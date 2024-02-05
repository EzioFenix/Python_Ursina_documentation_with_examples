from ursina import *

app = Ursina()

# Velocidad constante de movimiento del cubo
movement_speed = 0.1

# Límites de movimiento en el eje x
right_limit = 5
left_limit = -5

# Crea un cubo con textura de ladrillos
cube = Entity(model='cube', texture='brick', scale=(1,1,1))

def update():
    # Mueve el cubo en el eje x
    global movement_speed
    cube.x += movement_speed
    
    # Revisa si el cubo ha alcanzado alguno de los límites y cambia la dirección del movimiento
    if cube.x > right_limit or cube.x < left_limit:
        movement_speed *= -1

app.run()
