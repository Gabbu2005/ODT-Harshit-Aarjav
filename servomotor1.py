from machine import Pin, PWM
import time

servopin=Pin(4, Pin.OUT)
servo=PWM(servopin)



servo.freq(50)

# Function to set the servo angle
def set_servo_angle(angle):
    duty = int(40 + (angle / 180) * 115)
    servo.duty(duty)
    time.sleep(0.02)  # Small delay to allow the servo to move

# Example usage
while True:
    set_servo_angle(0)
    time.sleep(1)
    set_servo_angle(90)
    time.sleep(1)
    set_servo_angle(180)
    time.sleep(1)

# Write your code here :-)
