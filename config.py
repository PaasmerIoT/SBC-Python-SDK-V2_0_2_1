import serial
from deviceName import *

UserName = "E-mail Address" #your user name used in developer.paasmer.co for registration

feedname=("Feed1","Feed2","Feed3","feed4","feed5",...)  # Modify with the required feednames

feedtype=("sensor","sensor","sensor","actuator","actuator",...) # mention the feedtype as sensor/ actuatuor

feedpin=(2,22,5,6,32,...) # mention the pins used. ( Use Physical pins- RaspberryPi, BananaPi and OrangePi, Use GPIO pins for BeagleBone)

connectiontype = ("GPIO","GPIO","zigbee","GPIO","GPIO",...)

timePeriod = 5 #change the time delay(in seconds) as you required for sending sensor values to paasmer cloud

ser = 0 

#ser = serial.Serial("/dev/ttyUSB0",9600) # Specify the port in which ZigBee is connected ( Un comment this line Only if Zigbee is used)
