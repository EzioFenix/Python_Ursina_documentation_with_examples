from ursina import *

def update_slider_value():
    # Actualiza el valor del control deslizante y la longitud de la barra visual según el valor del control deslizante
    slider_value_text.text = f'Value: {int(slider.value)}'
    visual_bar.scale_x = slider.value / slider.max

def input(key):
    # Incrementa o decrementa el valor del control deslizante cuando se presionan las teclas de flecha
    if key == 'right arrow' and slider.value < slider.max:
        slider.value += slider.step
        update_slider_value()
    elif key == 'left arrow' and slider.value > slider.min:
        slider.value -= slider.step
        update_slider_value()

app = Ursina()

# Define el tamaño de la ventana que prefieras
window.size = (640, 360)
window.title = "Slider Control with Arrow Keys"

# Crea el control deslizante
slider = Slider(min=0, max=100, step=1, dynamic=True, horizontal=True)
slider.position = (0, -0.25)

# Crea una barra visual para representar el valor del control deslizante
visual_bar = Entity(model='quad', color=color.azure, scale=(0, 0.05, 1), origin=(-0.5, 0), x=-0.5)

# Crea un texto para mostrar el valor del control deslizante
slider_value_text = Text(text=f'Value: {int(slider.value)}', scale=2, position=(-0.5, 0.25))

# Actualiza la barra visual y el texto inicialmente
update_slider_value()

app.run()
