# -*- coding: utf-8 -*-
"""
Created on Sat Aug 27 14:48:26 2016

@author: Ben
"""
import serial
from struct import *

class buck():
    def __init__(self, COM):
        try:
            self.ser = serial.Serial(COM, timeout = .001)
            self.ser.baudrate = 9600
            self.Voltage = 0
            print('connected to buck')
        except:
            print('failed to connect to buck')
            pass
            
    def packet(self, val):
        i = int(1000*(val))
        byte2 = i>>8
        byte1 = i%256
        checksum = byte1^byte2
        buff = [0, 0, 0, byte1, byte2, checksum]
        #print(buff)
        return bytes(buff)
        
    def setVoltage(self, speed):
        self.speedcmd = speed
        try:
            self.ser.write(self.packet(speed))
           # print(self.speed)
            #print(self.ser.readline())
        except:
            pass
        
    def disable(self):
        buff = [0, 0, 0, 0, 0, 0]
        try:
            self.ser.write(buff)
        except:
            pass
