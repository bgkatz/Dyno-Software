# -*- coding: utf-8 -*-
"""
Created on Sat Aug 27 14:48:26 2016

@author: Ben
"""
import serial
from struct import *
import time

class absorber():
    def __init__(self, COM):
        try:
            self.speed = 0
            self.speedVec = [0]
            self.ser = serial.Serial(COM, timeout = .001)
            self.ser.baudrate = 115200
            self.speedcmd = 0
            self.torquecmd = 0
            print('conencted to absorber')
        except:
            print('failed to connect to absorber')
            pass
    def getSpeed(self):
        '''
        packet = [0, 0, 0, 0, 0, 0]
        try:
            while(self.ser.readable()):
                byte = self.ser.read()
                packet.append(ord(byte))
                packet = packet[1:7]
                startSeq = not packet[0] and not packet[1] and not packet[2]
                checksum = (packet[3]^packet[4])==packet[5]
                if(startSeq and checksum and sum(packet)>0):
                    val = (float((packet[4]<<8)+packet[3]))/50.0-700.0
                    #print(val)
                    self.speed = val
                    self.speedVec.append(self.speed)
                    self.ser.flushInput()
                    break
        except:
            '''
        self.speedVec.append(self.speed) #hold previous speed if packet is lost or something            
            #data = self.ser.readline()
            #self.speed = float(data)
            #self.speedVec.append(self.speed)
            
    def packet(self, val):
        i = int(10*(val+700))
        byte2 = i>>8
        byte1 = i&0xFF;
        checksum = byte1^byte2
        buff = [0, 0, 0, byte1, byte2, checksum]
        #print(buff)
        return bytes(buff)
        
    def setSpeed(self, speed):
        cmd_string = "%.4f" % speed
        cmd_string =  'setp ' + cmd_string + '\r'
        print(cmd_string)
        try:
            self.ser.write(bytes(cmd_string, 'utf-8'))
           # print(self.speed)
            #print(self.ser.readline())
        except:
            pass
        #self.getSpeed()
        self.ser.flushInput()

    def enterSpeedMode(self):
        try:
            self.ser.write(b'op speed\r')
        except:
            pass



    def enterTorqueMode(self):
        try:
            self.ser.write(b'op torque\r')
        except:
            pass

    def disable(self):
        self.torquecmd = 0
        self.enterTorqueMode()
        time.sleep(.02)
        #self.setSpeed(0.0)
    
