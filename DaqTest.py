# -*- coding: utf-8 -*-
"""
Created on Mon Feb  6 02:28:25 2017

@author: Ben
"""
import time
import UniversalLibrary as UL
import numpy


Gain = UL.BIP5VOLTS
Chan = 0
BoardNum = 0

n = 300
f = 5000


#print("DataVal:", DataValue, "volts:", engUnits, "Ratio:"  , DataValue/engUnits)


Options = UL.CONVERTDATA + UL.BACKGROUND + UL.SINGLEIO
ADData = numpy.zeros((n,), dtype=numpy.int16)


Status = UL.RUNNING
CurCount = 0
CurIndex = 0
start = time.time()

UL.cbAInScan(BoardNum, 0, 2, n, f, Gain, ADData, Options)
#Qwhile Status==UL.RUNNING:
 #   Status, CurCount, CurIndex = UL.cbGetStatus(BoardNum, Status, CurCount, CurIndex, UL.AIFUNCTION)
    #time2 = (time.time()-start)/n
    
time.sleep(n/f)
    #torqueVolts = UL.cbToEngUnits(BoardNum, Gain, int(ADData[0]))
    #currentVolts = UL.cbToEngUnits(BoardNum, Gain, int(ADData[2]))
    #voltageVolts = UL.cbToEngUnits(BoardNum, Gain, int(ADData[1]))
    #time.sleep(.000001)
torqueVolts = UL.cbToEngUnits(BoardNum, Gain, int(numpy.mean(ADData[0::3])))
voltageVolts = UL.cbToEngUnits(BoardNum, Gain, int(numpy.mean(ADData[1::3])))
currentVolts = UL.cbToEngUnits(BoardNum, Gain, int(numpy.mean(ADData[2::3])))
print(time.time()-start)
print(torqueVolts, currentVolts, voltageVolts)
print(ADData[0::3])
#print(torqueVolts, currentVolts, voltageVolts)

#print("time1:  ", time1, "time2:  ", time2)

#print(mean, "   ", numpy.mean(ADData))

#print(engUnits, UL.cbToEngUnits(BoardNum, Gain, numpy.mean(ADData)))
