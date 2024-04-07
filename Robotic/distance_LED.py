from machine import Pin, time_pulse_us, ADC, PWM
from time import sleep_us, sleep
import machine
import utime, math
import neopixel

# Configuración de la matriz LED
NUM_LEDS = 16  # Número total de LEDs en la matriz
PIN = 4  # Pin GPIO donde está conectada la matriz (D5 en NodeMCU)
np = neopixel.NeoPixel(machine.Pin(PIN), NUM_LEDS)

# Función para establecer el color de un LED en una posición específica
def set_pixel_color(x, y, color):
    if 0 <= x < 4 and 0 <= y < 4:
        index = y * 4 + x
        np[index] = color
        np.write()
        
def sonrisa():
    set_pixel_color(0, 1, (25, 50, 0)) 
    set_pixel_color(2, 0, (25, 50, 0))
    set_pixel_color(1, 0, (25, 50, 0))
    set_pixel_color(3, 1, (25, 50, 0))
    #Leds de los ojos
    set_pixel_color(1, 3, (0, 25, 0))
    set_pixel_color(2, 3, (0, 25, 0))
    set_pixel_color(1, 2, (0, 25, 0))
    set_pixel_color(2, 2, (0, 25, 0))
    
def sad():
    #Leds de los ojos
    set_pixel_color(1, 3, (255, 0, 0))
    set_pixel_color(2, 3, (255, 0, 0))
    # Leds de la sonrisa
    set_pixel_color(0, 0, (255, 0, 0)) 
    set_pixel_color(1, 1, (255, 0, 0))
    set_pixel_color(2, 1, (255, 0, 0))
    set_pixel_color(3, 0, (255, 0, 0))
    
def clear():
    for i in range(NUM_LEDS):
        np[i] = (0, 0, 0)
    np.write()


#led = machine.Pin(2, Pin.OUT)
# pwm
pwm = PWM(Pin(5), freq=50, duty=0)


def measure_distance(TRIGGER_PIN,ECHO_PIN):
    
    # Initialize trigger and echo pins
    trigger = machine.Pin(TRIGGER_PIN, Pin.OUT)
    echo = machine.Pin(ECHO_PIN, Pin.IN)

    # Ensure trigger is low initially
    trigger.value(0)
    sleep_us(2)

    # Send a 10 microsecond pulse to the trigger pin
    trigger.value(1)
    sleep_us(10)
    trigger.value(0)

    # Measure the duration of the echo pulse (in microseconds)
    pulse_duration = time_pulse_us(echo, 1)

    # Calculate the distance (in centimeters) using the speed of sound (343 m/s)
    distance = pulse_duration * 0.0343 / 2
    return distance

while True:
    data = measure_distance(14, 12)
    sleep_us(2)
    clear()
    if data < 50:
        sad()
    else:    
        sonrisa()