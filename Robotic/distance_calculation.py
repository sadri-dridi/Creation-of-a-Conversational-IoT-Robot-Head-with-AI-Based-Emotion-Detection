import machine
from machine import Pin, time_pulse_us, ADC
from time import sleep_us, sleep

def measure_distance():
    # Initialize trigger and echo pins
    trigger = machine.Pin(14, Pin.OUT)
    echo = machine.Pin(12, Pin.IN)
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
    data = measure_distance()
    if data > 5:
        print("distance =", data)
    else:
        print(data)