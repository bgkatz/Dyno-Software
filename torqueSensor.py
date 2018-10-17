
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
        	self.ser = serial.Serial(port, timeout = .01)
        	self.ser.baudrate = 115200
        	print('connected to the torque sensor')
        except:
        	print('failed to connect to the torque sensor')
        	pass


        
    def sampleTorque(self):
    	try:
            
            if(self.ser.readable()):
                bytes_available = self.ser.in_waiting
                #print(bytes_available)
                packet_done = False
                packet = []
                while (not packet_done):
                    byte = list(self.ser.read())
                    packet.append(byte[0])
                    if(packet[0] != 10):
                        packet.pop(0)
                    elif(packet[0] == 10 and packet[-1] == 10 and len(packet)>1):
                        packet_done = True
                
                #line = self.ser.readline()
                #line = self.ser.readline()
	    		#print(line)
            #self.ser.flushInput()
            #line = 0
            print(bytes_available, packet)
            self.Torque = int(bytes(packet[1:-2]))
            self.TorqueVec.append(float(self.Torque) / 1000.0)
	    		
    	except:
            print("Something went wrong reading the torque sensor")
            self.TorqueVec.append(self.Torque)

 
        
    def getTorqueVec(self):
        return self.TorqueVec
        
