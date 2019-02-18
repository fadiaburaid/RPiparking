import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM) # Broadcom pin-numbering scheme
GPIO.setup(14, GPIO.OUT) # RED LED pin set as output
GPIO.setup(15, GPIO.OUT) # YELLOW LED pin set as output
GPIO.setup(18, GPIO.OUT) # GREEN LED pin set as output
GPIO.setup(23, GPIO.OUT) # BUZZER pin set as output
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Button pin set as input w/ pull-up
GPIO.output(18, GPIO.HIGH)
GPIO.output(14, GPIO.LOW)
GPIO.output(15, GPIO.LOW)
GPIO.output(23, GPIO.LOW)
print("Here we go! Press CTRL+C to exit")
try:
    while 1:
        num = 10
        if GPIO.input(24): # button is released
           time.sleep(0.05)
        else: # button is pressed:
           GPIO.output(18, GPIO.LOW)
           time.sleep(0.5)
           GPIO.output(15, GPIO.HIGH)
           time.sleep(1)
           GPIO.output(15, GPIO.LOW)
           GPIO.output(14, GPIO.HIGH)
           while (0 < num) :
             GPIO.output(23, GPIO.HIGH)
             time.sleep(0.5)
             GPIO.output(23, GPIO.LOW)
             time.sleep(0.5)
             num = num - 1
             
           GPIO.output(14, GPIO.LOW)
           time.sleep(0.5)                   
           GPIO.output(15, GPIO.HIGH)
           time.sleep(1)
           GPIO.output(15, GPIO.LOW)
           GPIO.output(18, GPIO.HIGH)
except KeyboardInterrupt: # If CTRL+C is pressed, exit cleanly:
    GPIO.cleanup() # cleanup all GPIO
