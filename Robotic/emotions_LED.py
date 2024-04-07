import machine
import neopixel
import time
from machine import Pin

#Matriz
# Configuración de la matriz LED
NUM_LEDS = 16  # Número total de LEDs en la matriz
PIN = 14  # Pin GPIO donde está conectada la matriz (D5 en NodeMCU)
np = neopixel.NeoPixel(machine.Pin(PIN), NUM_LEDS)

#Ultrasonido
# Definir pines GPIO para el sensor de ultrasonido
TRIGGER_PIN = 12
ECHO_PIN = 4
# Configurar pines GPIO
trigger = Pin(TRIGGER_PIN, Pin.OUT)
echo = Pin(ECHO_PIN, Pin.IN)


# Función para establecer el color de un LED en una posición específica
def set_pixel_color(x, y, color):
    if 0 <= x < 4 and 0 <= y < 4:
        index = y * 4 + x
        np[index] = color
        np.write()
        
def feliz():
    # Leds de la sonrisa
    set_pixel_color(3, 2, ( 0, 25, 0)) 
    set_pixel_color(2, 1, ( 0, 25, 0))
    set_pixel_color(1, 1, ( 0, 25, 0))
    set_pixel_color(0, 2, ( 0, 25, 0))

#def triste():
    # Leds de la sonrisa
    #set_pixel_color(3, 2, (0, 0, 10)) 
    #set_pixel_color(2, 1, (0, 0, 10))
    #set_pixel_color(1, 1, (0, 0, 10))
    #set_pixel_color(0, 2, (0, 0, 10))


def apagarLeds():
    # Apagar todos los LEDs
    for i in range(NUM_LEDS):
        np[i] = (0, 0, 0)
        np.write()

# Función para medir la distancia
def get_distance():
    # Generar pulso de disparo
    trigger.off()
    time.sleep_us(2)
    trigger.on()
    time.sleep_us(5)
    trigger.off()

    # Medir el tiempo de ida y vuelta del pulso
    while echo.value() == 0:
        pulse_start = time.ticks_us()
    while echo.value() == 1:
        pulse_end = time.ticks_us()

    # Calcular la duración del pulso
    pulse_duration = pulse_end - pulse_start

    # Calcular la distancia en centímetros
    distance = pulse_duration * 0.0343 / 2

    return distance

# Bucle principal
while True:
    try:
        distance = get_distance()
        print("Distancia:", distance, "cm")
        
        if distance < 20:
            
            feliz()
            time.sleep(1)
        else:
            
            apagarLeds()
            time.sleep(1)

    except KeyboardInterrupt:
        print("Programa detenido por el usuario")
        break 