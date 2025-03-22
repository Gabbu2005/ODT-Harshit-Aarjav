from machine import Pin, PWM, TouchPad
import time


pwm= PWM(Pin(14))
pwm2= PWM(Pin(27))
touch1= TouchPad(Pin(12))


pwm.freq(32000)  
pwm2.freq(32000)
def play_wav_pwm(filename):
    with open(filename, "rb") as file:
# Skips WAV header
        file.seek(44)  

        while True:
            data = file.read(512)  
            if not data:
                break

            for byte in data:
# Scales 8-bit to 10-bit PWM
                duty = int(byte / 255 * 1023)
                pwm.duty(duty)
                pwm2.duty(duty) 
                time.sleep(1 / 32000) 

while True:
    time.sleep(0.5)
    print(touch1.read())
    if int(touch1.read())<380:
        print("Under Your Spell")    
        print("🎶 Playing WAV via PWM...")
        play_wav_pwm("/monster3.wav")  
