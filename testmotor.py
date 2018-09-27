# -*- coding: utf-8 -*-
"""
Created on Sat Aug 27 14:48:26 2016

@author: Ben
"""
import serial
from struct import *

class testmotor():
    def __init__(self, COM):
        try:
            self.ser = serial.Serial(COM, timeout = .001)
            self.ser.baudrate = 115200
            self.period = 0
            self.voltage = 0;
            print('connected to test motor')
        except:
            print('failed to connect to test motor')
            pass
            
    def sendPeriod(self, period):
        i = int(25*(period))
        byte2 = i>>8
        byte1 = i&0xFF
        checksum = byte1^byte2
        buff = [0, 0, 10, byte1, byte2, 0, 0, 0, 0, checksum]
        #print('sentPeriod')
        try:
            self.ser.write(bytes(buff))

        except:
            pass
        
    def sendVoltage(self, voltage):
        i = int(1000*(voltage))
        byte2 = i>>8
        byte1 = i&0xFF
        checksum = byte1^byte2
        buff = [0, 0, 20, byte1, byte2, 0, 0, 0, 0, checksum]
        #print('sentVoltage')
        try:
            self.ser.write(bytes(buff))
 
        except:
            pass
        
    def sendCAN(self, cmd, p1, p2):
        i_cmd = (int(cmd*512))+(1<<15)
        i_p1 = (int(p1*16))+(1<<15)
        i_p2 = (int(p2*16))+(1<<15)
        cmd_byte2 = i_cmd>>8
        cmd_byte1 = i_cmd&0xFF
        p1_byte2 = i_p1>>8
        p1_byte1 = i_p1&0xFF
        p2_byte2 = i_p2>>8
        p2_byte1 = i_p2&0xFF
        checksum = cmd_byte1^cmd_byte2^p1_byte1^p1_byte2^p2_byte1^p2_byte2
        buff = [0, 0, 30, cmd_byte1, cmd_byte2, p1_byte1, p1_byte2, p2_byte1, p2_byte2, checksum]
        try:
            self.ser.write(bytes(buff))
        except:
            pass
        #print(self.ser.readline())
        
        
    def setVoltage(self, voltage):
        self.voltage = voltage
        self.sendVoltage(voltage)

    def setPeriod(self, period):
        self.period = period
        self.sendPeriod(period)
    
    def setCANCmd(self, cmd, p1, p2):
        self.CANCmd = cmd
        self.p1 = p1
        self.p2 = p2
        self.sendCAN(cmd, p1, p2)
        
        
    def disable(self):
        buff = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        try:
            self.ser.write(buff)
        except:
            pass
