
import numpy
import time
import serial
from struct import*



class torqueSensor():
    def __init__(self, port):
        self.TorqueVec = [0]
        self.Torque = 0
        self.TorqueOffset = 0
        try:
        	self.ser = serial.Serial(port, timeout = .05)
        	self.ser.baudrate = 115200
        	print('connected to the torque sensor')
        except:
        	print('failed to connect to the torque sensor')
        	pass


        
    def sampleTorque(self):
    	try:
    		if(self.ser.readable()):
	    		line = self.ser.readline()
	    		line = self.ser.readline()
	    		#print(line)
	    	self.ser.flushInput()
	    	self.Torque = int(line)
	    	self.TorqueVec.append(float(self.Torque) / 1000.0)
	    		
    	except:
            self.TorqueVec.append(self.Torque)
        
 
        
    def getTorqueVec(self):
        return self.TorqueVec
        
