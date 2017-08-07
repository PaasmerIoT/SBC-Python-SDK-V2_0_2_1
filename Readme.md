# SBC-Python-SDK-V_2.0.2.1
**Paasmer IoT SBC-Python-SDK-V_2.0.2.1** for Single Board Computers Running Linux

## Overview
The **Paasmer SBC-Python-SDK-V_2.0.2.1** for **Single Board Computers (SBC)** like Raspberry-PI, Banana-PI, Orange-PI, Odroidxu4 and BeagleBone is a collection of source files that enables you to connect to the Paasmer IoT Platform. It includes the transport client for **MQTT** with **TLS** support.  It is distributed in source form and intended to be built into customer firmware along with application code, other libraries and RTOS.This SDK is equipped with the Zigbee support along with Board GPIO's.

## Features
The **SBC-Python-SDK-V_2.0.2.1** simplifies access to the Pub/Sub functionality of the **Paasmer IoT** broker via **MQTT**.The SDK has been tested to work on the **Raspberry PI 3, Banana-PI, Orange-PI, Odroidxu4 and BeagleBone**.

## MQTT Connection
The **SBC-Python-SDK-V_2.0.2.1** provides functionality to create and maintain a mutually authenticated TLS connection over which it runs **MQTT**. This connection is used for any further publish operations and allow for subscribing to **MQTT** topics which will call a configurable callback function when these topics are received.

## Protocols Supported
The **SBC-Python-SDK-V_2.0.2.1** is equipped with the Zigbee support along with Board GPIO's.

## Pre Requisites
Registration on the [PAASMER portal](http://developers.paasmer.co) is necessary to connect the devices to the **Paasmer IoT Platform** .The SDK has been tested on the Raspberry PI 3 Banana-PI, Orange-PI, Odroidxu4 and BeagleBone. Python 2.7 needs to be pre installed on the devices. 

##  Optional Requisites
In order to use the Zigbee the following is required.

* Single Board Computer

* Arduino UNO Board.

* 2 ZigBee modules.

* XCTU Software installed on your system for ZigBee configuration. [XCTU software](https://www.digi.com/products/xbee-rf-solutions/xctu-software/xctu)

* Lastest version of Arduino IDE to installed on your computer. [Arduino software](https://www.arduino.cc/en/main/software)

# Installation

* Download the SDK or clone it using the command below.

```
$ git clone https://github.com/PaasmerIoT/SBC-Python-SDK-V_2.0.2.1
$ cd SBC-Python-SDK-V_2.0.2.1
```

## ZigBee Configuration (Optional)

To establish, the ZigBee protocol the 2 ZigBee modules are to configured as a Coordinator and a Router. The ZigBee at the Single Board Computer side is to be configured as a Coordinator and the one at the Arduino side as a Router. Use XCTU software to Configure the ZigBee's as explained in the `ZigBEE_config.pdf` file.

The installation part is to be done in two parts, like

* Arduino  

* Single Board Computer
 
## Arduino 

* Connect the ZigBee Router device to the Arduino UNO as give below

| Arduino   | XBee |
| --------- | -----|
| 5V        | 5V   |
| GND       | GND  |
| TX        | RX   |
| RX        | TX   |


* Open a new Sketch, Copy and Paste from the `ZigBee.ino` file in `<Arduino Sketch_DIR>/`.

* Connect the Arduino UNO board to your system, open the Arduino IDE and click on the `TOOLS` icon, select the `Board` as **Arduino/Genuino UNO** and select the port in which the board is connected in the `Port` option. 

* Also edit the `Config.h` in the Arduino Sketch similar to our `config.py` file in RaspberryPi. The code sample is as below,

```
#define devicename "Zigbee" //your device name

#define timePeriod 2 //change the time delay as you required for sending sensor values to paasmer cloud

char feedname[][10]={"Feed1","Feed2","Feed3","feed4","feed5","feed6"};

String feedtype[]={"sensor","sensor","sensor","actuator","actuator","actuator"};

String connectiontype[]= {"GPIO","GPIO","zigbee","GPIO","GPIO","zigbee"};

int feedpin[]={2,4,5,6,32,8};
```
* Save and Run the code in Arduino UNO.

## Single Board Computer Installation


* To connect the device to Paasmer IoT Platform, the following steps need to be performed.

```
$ sudo chmod 777 ./*
$ sudo ./install.sh
```
This will take some time to install the required softwares and packages.

* To register the device to the Paasmer IoT Platform, the following command need to be executed.

```
$ sudo ./paasmerDeviceRegistration.sh
```

This will ask for the device name. Give a unique device name for your device and that must be alphanumeric[a-z A-Z 0-9].

* Upon successful completion of the above command, the following commands need to be executed.
```
echo "-->  1) sudo su "
echo "-->  2) source ~/.bashrc "
echo "-->  3) PAASMER_THING "
echo "-->  4) PAASMER_POLICY "
echo "-->  5) sed -i 's/alias PAASMER/#alias PAASMER/g' ~/.bashrc "
echo "-->  6) exit "
$ exit
```


* Edit the config.py file to include the user name(Email),feed names , feed types, connnectiontype and feed pin details. 

```c
UserName = "E-Mail Address" #your user name used in developer.paasmer.co for registration

feedname=("Feed1","Feed2","Feed3","feed4","feed5","feed6")  # Modify with the required feednames

feedtype=("sensor","sensor","sensor","actuator","actuator","actuator") # mention the feedtype as sensor/ actuatuor

feedpin=(2,22,5,6,32,8) # mention the pins used. ( Use Physical pins- RaspberryPi, BananaPi and OrangePi, Use GPIO pins for BeagleBone)

connectiontype = ("GPIO","GPIO","zigbee","GPIO","GPIO","zigbee") 

timePeriod = 5 #change the time delay(in seconds) as you required for sending sensor values to paasmer cloud

ser = 0  # if you are using GPIO pins only. Comment this line if ZigBee intefacing is required

#ser = serial.Serial("/dev/ttyUSB0",9600)  # for GPIO and ZigBee Interface . Comment this line if only GPIO is used. 

```

* Connect the ZigBee Coordinator device to the RaspberryPi through the USB2.0 cable. (Only is ZigBee is used)

* Go to the diectory below.

```
$ cd samples/basicPubSub/
```
      
* Run the code using the command below.

```
$ sudo python basicPubSub.py
```

* The device would now be connected to the Paasmer IoT Platform and publishing sensor values are specified intervals.

## Support

The support forum is hosted on the GitHub, issues can be identified by users and the Team from Paasmer would be taking up requests and resolving them. You could also send a mail to support@paasmer.co with the issue details for quick resolution.

## Note

* The Paasmer IoT SBC-Python-SDK-V_2.0.2.1 utilizes the features provided by AWS-IOT-SDK for Python.
