from path import *
from config import *
from deviceType import *
import os
import serial
import time

def gpioSetup():
#       if deviceType == "raspberrypi" or deviceType== "bananapi" or deviceType=="orangepi" or deviceType== "ordroidxu4" :
        if ser :
			ser.isOpen()


def gpio_read(pinNum):
	n= "Read pin " + str(pinNum) + "*"
	print n
	ser.write(n)
	time.sleep(.5)
	incoming = ser.read()
	return int(incoming )

def zigbeeWrite(zigbee):
	ser.write(zigbee)

def gpioModesetup(pinNum, mode) :
	if deviceType == "raspberrypi" or deviceType== "bananapi" or deviceType=="orangepi" or deviceType== "ordroidxu4" :
		if mode== "OUT" :
			command= "gpio -1 mode " + str(pinNum) + " out"
			os.system (command)
			command="\0"
		elif mode == "IN" :
			command= "gpio -1 mode " + str(pinNum) + " in"
			os.system (command)
			command="\0"
	elif deviceType == "beaglebone" :
		if mode== "OUT" :
			command= "sudo echo " + str(pinNum) + " > /sys/class/gpio"
			os.system (command)
			command="\0"
			command= "sudo echo out > /sys/class/gpio/gpio" + str(pinNum) + "/direction"
			os.system (command)
			command="\0"
		elif mode == "IN" :
			command= "sudo echo " + str(pinNum) + " > /sys/class/gpio"
			os.system (command)
			command="\0"
			command= "sudo echo in > /sys/class/gpio/gpio" + str(pinNum) + "/direction"
			os.system (command)
			command="\0"

def gpioWrite(pinNum, state) :
	if deviceType == "raspberrypi" or deviceType== "bananapi" or deviceType=="orangepi" or deviceType== "ordroidxu4" :
		command = "gpio -1 write " + str(pinNum) + " " +  str(state)
		print(command) 
		os.system(command)
		command="\0"
	elif deviceType == "beaglebone" :
		command = "sudo echo " + str(state) + " > /sys/class/gpio/gpio" +  str(pinNum) + "/value"
		os.system(command)
		command="\0"
def gpioRead(pinNum) :
	res=0
	if deviceType == "raspberrypi" or deviceType== "bananapi" or deviceType=="orangepi" or deviceType== "ordroidxu4" :
		command = "gpio -1 read " + str(pinNum)
		data = os.popen(command).readlines()
		command = "\0"
		res = int(data[0])
	elif deviceType == "beaglebone" :
		command = "sudo cat /sys/class/gpio/gpio" + str(pinNum) + "/value"
		data = os.popen(command).readlines()
		command = "\0"
	res = int(data[0])
	return res
		

