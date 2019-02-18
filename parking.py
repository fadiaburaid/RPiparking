import RPi.GPIO as GPIO
import wiringpi as wiringpi  
import time

wiringpi.wiringPiSetupGpio()
GPIO.setmode(GPIO.BCM) # Broadcom pin-numbering scheme
wiringpi.pinMode(13,2)
wiringpi.pwmSetMode(0)
wiringpi.pwmSetClock(384)
wiringpi.pwmSetRange(1000)
wiringpi.pwmWrite(13,120)
GPIO.setup(14, GPIO.OUT) # LED a pin set as output
GPIO.setup(15, GPIO.OUT) # LED b pin set as output
GPIO.setup(18, GPIO.OUT) # LED c pin set as output
GPIO.setup(23, GPIO.OUT) # LED d pin set as output
GPIO.setup(24, GPIO.OUT) # LED e pin set as output
GPIO.setup(25, GPIO.OUT)# LED f pin set as output
GPIO.setup(8, GPIO.OUT) # LED g pin set as output
GPIO.setup(2, GPIO.IN)# set GPIO 2 as an input for proximity sensor 1. 
GPIO.setup(3, GPIO.IN)# set GPIO 3 as an input for proximity sensor 2. 
GPIO.setup(4, GPIO.OUT)# set GPIO 4 as an output for servo. 


def disp(int):
  if int==0:
    num0()
  elif int==1:
    num1()
  elif int==2:
    num2()
  elif int==3:
    num3()
  elif int==4:
    num4()
  elif int==5:
    num5()
  elif int==6:
    num6()
  elif int==7:
    num7()
  elif int==8:
    num8()
  elif int==9:
    num9()
  return;

def num0():
  GPIO.output(14, GPIO.HIGH) # LED a pin 
  GPIO.output(15, GPIO.HIGH) # LED b pin 
  GPIO.output(18, GPIO.HIGH) # LED c pin 
  GPIO.output(23, GPIO.HIGH) # LED d pin 
  GPIO.output(24, GPIO.HIGH) # LED e pin 
  GPIO.output(25, GPIO.HIGH) # LED f pin 
  GPIO.output(8, GPIO.LOW)  # LED g pin
def num1():
  GPIO.output(14, GPIO.LOW) # LED a pin 
  GPIO.output(15, GPIO.HIGH) # LED b pin 	
  GPIO.output(18, GPIO.HIGH) # LED c pin 
  GPIO.output(23, GPIO.LOW) # LED d pin 
  GPIO.output(24, GPIO.LOW) # LED e pin 
  GPIO.output(25, GPIO.LOW) # LED f pin 
  GPIO.output(8, GPIO.LOW)  # LED g pin
def num2():
  GPIO.output(14, GPIO.HIGH) # LED a pin 
  GPIO.output(15, GPIO.HIGH) # LED b pin 
  GPIO.output(18, GPIO.LOW) # LED c pin 
  GPIO.output(23, GPIO.HIGH) # LED d pin 
  GPIO.output(24, GPIO.HIGH) # LED e pin 
  GPIO.output(25, GPIO.LOW) # LED f pin 
  GPIO.output(8, GPIO.HIGH)  # LED g pin
def num3():
  GPIO.output(14, GPIO.HIGH) # LED a pin 
  GPIO.output(15, GPIO.HIGH) # LED b pin 
  GPIO.output(18, GPIO.HIGH) # LED c pin 
  GPIO.output(23, GPIO.HIGH) # LED d pin 
  GPIO.output(24, GPIO.LOW) # LED e pin 
  GPIO.output(25, GPIO.LOW) # LED f pin 
  GPIO.output(8, GPIO.HIGH)  # LED g pin
def num4():
  GPIO.output(14, GPIO.LOW) # LED a pin 
  GPIO.output(15, GPIO.HIGH) # LED b pin 
  GPIO.output(18, GPIO.HIGH) # LED c pin 
  GPIO.output(23, GPIO.LOW) # LED d pin 
  GPIO.output(24, GPIO.LOW) # LED e pin 
  GPIO.output(25, GPIO.HIGH) # LED f pin 
  GPIO.output(8, GPIO.HIGH)  # LED g pin
def num5():
  GPIO.output(14, GPIO.HIGH) # LED a pin 
  GPIO.output(15, GPIO.LOW) # LED b pin 
  GPIO.output(18, GPIO.HIGH) # LED c pin 
  GPIO.output(23, GPIO.HIGH) # LED d pin 
  GPIO.output(24, GPIO.LOW) # LED e pin 
  GPIO.output(25, GPIO.HIGH) # LED f pin 
  GPIO.output(8, GPIO.HIGH)  # LED g pin
def num6():
  GPIO.output(14, GPIO.HIGH) # LED a pin 
  GPIO.output(15, GPIO.LOW) # LED b pin 
  GPIO.output(18, GPIO.HIGH) # LED c pin 
  GPIO.output(23, GPIO.HIGH) # LED d pin 
  GPIO.output(24, GPIO.HIGH) # LED e pin 
  GPIO.output(25, GPIO.HIGH) # LED f pin 
  GPIO.output(8, GPIO.HIGH)  # LED g pin
def num7():
  GPIO.output(14, GPIO.HIGH) # LED a pin 
  GPIO.output(15, GPIO.HIGH) # LED b pin 
  GPIO.output(18, GPIO.HIGH) # LED c pin 
  GPIO.output(23, GPIO.LOW) # LED d pin 
  GPIO.output(24, GPIO.LOW) # LED e pin 
  GPIO.output(25, GPIO.LOW) # LED f pin 
  GPIO.output(8, GPIO.LOW)  # LED g pin
def num8():
  GPIO.output(14, GPIO.HIGH) # LED a pin 
  GPIO.output(15, GPIO.HIGH) # LED b pin 
  GPIO.output(18, GPIO.HIGH) # LED c pin 
  GPIO.output(23, GPIO.HIGH) # LED d pin 
  GPIO.output(24, GPIO.HIGH) # LED e pin 
  GPIO.output(25, GPIO.HIGH) # LED f pin 
  GPIO.output(8, GPIO.HIGH)  # LED g pin
def num9():
  GPIO.output(14, GPIO.HIGH) # LED a pin 
  GPIO.output(15, GPIO.HIGH) # LED b pin 
  GPIO.output(18, GPIO.HIGH) # LED c pin 
  GPIO.output(23, GPIO.HIGH) # LED d pin 
  GPIO.output(24, GPIO.LOW) # LED e pin 
  GPIO.output(25, GPIO.HIGH) # LED f pin 
  GPIO.output(8, GPIO.HIGH)  # LED g pin
print("Here we go! Press CTRL+C to exit")
try:
    num9()   
    num=9
    disp(num)
    while 1:
      if GPIO.input(2)&GPIO.input(3): # sensor2 & sensor3 are not detected
        time.sleep(0.05)
      elif ~GPIO.input(2)& GPIO.input(3)&(num!=0):
        wiringpi.pwmWrite(13,75)
        num=num-1
        disp(num)
        while GPIO.input(3):
          time.sleep(0.05)
        wiringpi.pwmWrite(13,120)
        time.sleep(2) 
      elif ~GPIO.input(3)& GPIO.input(2)&(num!=9):
        wiringpi.pwmWrite(13,75)
        num=num+1
        disp(num)
        while GPIO.input(2):
          time.sleep(0.05)
        wiringpi.pwmWrite(13,120)
        time.sleep(2)
        
except KeyboardInterrupt: # If CTRL+C is pressed, exit cleanly:
    GPIO.cleanup() # cleanup all GPIO
