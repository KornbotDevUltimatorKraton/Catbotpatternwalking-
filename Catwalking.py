import pyfirmata 
import time 
import numpy as np 
import math 
from multiprocessing import Process 
import itertools
try: 
  hardware = pyfirmata.ArduinoMega("/dev/ttyACM0")
  print("Catbot main body hardware connection successfully connected !")
except: 
  print("Hardware connection error resouting the serial communication...")
  try: 
     hardware = pyfirmata.ArduinoMega("/dev/ttyACM1")
     print("Main body hardware serial rerouting  connection successfully!")
  except: 
     print("Main serial error please check the physical hardware!")
  # USB
try: 
  hardware2 = pyfirmata.Arduino("/dev/ttyUSB0") 
  print("Catbot seccond body hardware connection successfully connected !")
except:  
  print("Hardware seccond connection error resouting the serial communication...")
  try: 
     hardware2 = pyfirmata.Arduino("/dev/ttyUSB0")
     print("Main body hardware serial rerouting  connection successfully!")
  except: 
     print("Seccond serial error please check the physical hardware!")
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

 # X axis  Gyrocontrol 
#Head 
Head = hardware.get_pin('d:8:s')
#Shoulder X - Left
#ShoulderLeft = hardware.get_pin('d:5:s')
#Shoulder X - left 
ShoulderRight = hardware.get_pin('d:4:s')
#Hip X - Left 
HipLeft = hardware.get_pin('d:3:s')
#Hip X - Right
#HipRight = hardware.get_pin('d:2:s') 
#Elbow X - left 
#ElbowLeft = hardware.get_pin('d:14:s')
#Elbow X - Right
ElbowRight = hardware.get_pin('d:11:s')
#Abduct knee X - Left 
Abductknee2Left = hardware.get_pin('d:7:s') 
Abductknee3Left = hardware2.get_pin('d:4:s')
#Abduct Knee Y - Right 
#Abductknee3Right = hardware2.get_pin('d:7:s')
#Abductknee2Right = hardware2.get_pin('d:8:s')
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>$
                        # Z - axis Gyrocontrol 
#Headz = hardware.get_pin('d:15:s')
def FrontRight_leg():
      for s in itertools.count():
           for i in range(1,60):
                  ShoulderRight.write(30 + 1.5*i)
                  ElbowRight.write(120 - i/2)
                  time.sleep(0.006)      

           for i in range(120,30,-1):
                  ShoulderRight.write(i)
                  if i < 60:
                     ElbowRight.write(90)
                  else: 
                     ElbowRight.write(i)  
                  time.sleep(0.006)
def BackLeft_leg(): 
     for q in itertools.count():
             for r in range(90,60,-1): 
                  HipLeft.write(r)
                  Abductknee2Left.write(180)
                  Abductknee3Left.write(r-50)
                  time.sleep(0.0118)
             for r in range(60,120): 
                  HipLeft.write(r)
                  Abductknee2Left.write(170)
                  Abductknee3Left.write(r+50)
                  time.sleep(0.012)
for w in itertools.count():
           Head.write(140)         
           p1 = Process(target=FrontRight_leg)
           p1.start()
           p2 = Process(target=BackLeft_leg)
           p2.start() 
           p1.join() 
           p2.join()
