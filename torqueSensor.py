
import numpy
import time
import serial
from struct import*



class torqueSensor():
    def __init__(self, port):
        self.TorqueVec = [0]
        self.Torque = 0
        self.data = 0
        self.TorqueOffset = 0
        self.val = 0
        try:
        	self.ser = serial.Serial(port, timeout = .1)
        	self.ser.baudrate = 115200
        	print('connected to the torque sensor')
        except:
        	print('failed to connect to the torque sensor')
        	pass


        
    def sampleTorque(self):
    	try:
            if(self.ser.readable()):
                val = self.ser.readline()
                self.data = int(val)#ord(val) - 128;
            while(self.ser.in_waiting > 16):    # clear the buffer without cropping packets
                self.ser.readline()

            self.Torque = self.data/1000.0
            self.TorqueVec.append(self.Torque) 
	    		
    	except:
            print("Something went wrong reading the torque sensor")
            self.TorqueVec.append(self.Torque)

    def continuousSample(self):
        while(1):
            try:
               self. val = self.ser.readline()
               self.data = int(self.val)
            except:
                pass
            self.Torque = self.data/1000.0
            self.TorqueVec.append(self.Torque)
        
    def getTorqueVec(self):
        return self.TorqueVec
        
