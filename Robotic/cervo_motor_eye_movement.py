import machine
from machine import Pin, PWM
import utime

# Servo range for three servomotors
servo_a_range = [0, 180]  # Define as required for each servo
servo_b_range = [0, 180]  # Example ranges
servo_c_range = [0, 180]  # Example ranges

# GPIO Pins where the servos are connected (update these according to your setup)
servo_pins = {'A': 15, 'B': 5, 'C': 4}

# PWM instances for each servo
pwms = {
    'A': PWM(Pin(servo_pins['A']), freq=50, duty=0),
    'B': PWM(Pin(servo_pins['B']), freq=50, duty=0),
    'C': PWM(Pin(servo_pins['C']), freq=50, duty=0)
}

# Function to convert angle to duty cycle
def angle_to_duty(angle):
    duty_for_0_degrees = 40
    duty_for_180_degrees = 190
    duty_range = duty_for_180_degrees - duty_for_0_degrees
    duty = duty_for_0_degrees + (angle / 180.0) * duty_range
    return int(duty)

# Function to command a servo to an angle within the limited range
def moveServo(servo_id, position):
    servo_range = {
        'A': servo_a_range,
        'B': servo_b_range,
        'C': servo_c_range
    }
    
    if servo_range[servo_id][0] <= position <= servo_range[servo_id][1]:
        pwm = pwms[servo_id]
        pwm.duty(angle_to_duty(position))
        utime.sleep(1)  # Give the servo time to move
        print("Servo", servo_id, "Angle:", position)
    else:
        print("Position out of range for Servo", servo_id, ". Please keep between", servo_range[servo_id][0], "and", servo_range[servo_id][1], "degrees.")

# Test the servos within the restricted range
#moveServo('A', 30) #extreme right of our x-axis
#moveServo('B', 20) # looking up max
#moveServo('C', 90) #fully closed eye / moveServo('C', 62) naturally closed eye
#utime.sleep(1)
#moveServo('B', 80) # looking at the center: y-axis at 0
#utime.sleep(1)
#moveServo('A', 100) #max eye left x-axis
#moveServo('B', 100) #looking down max
#moveServo('C', 45) #natural open eye
#utime.sleep(1)
#moveServo('A', 120)


#blinking function
while True:
    moveServo('C', 90)
    moveServo('C', 45)
    utime.sleep(1)
    moveServo('A', 30)
    moveServo('A', 100)
    utime.sleep(1)
    moveServo('B', 20)
    moveServo('B', 100)
    

# Test a servo outside the restricted range
#moveServo('A', 50)  # This should not move servo A and print a message instead