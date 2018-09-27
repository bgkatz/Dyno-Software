

import time

class Sequence():
    def __init__(self, times = 0, speeds = 0, cmds = 0, voltages = 0, flag = 0, p1 = 0, p2 = 0, cmdType = 0):
        self.times = times
        self.speeds = speeds
        self.cmds = cmds
        self.voltages = voltages
        self.flag = flag
        self.p1 = p1;
        self.p2 = p2;
        self.cmdType = cmdType
        self.tElapsed = 0
        self.startTime = 0
        self.index = 0
        self.speedSet = 0
        self.cmdSet = 0
        self.voltageSet = 0
        self.flagSet = 0
        self.p1Set = 0
        self.p2Set = 0
        self.enabled = False
        self.length = 0
        
        
    def start(self):
        self.startTime = time.time()
        self.length = len(self.times)
        self.enabled = True
        print('Sequence Started')
        
    def stop(self):
        self.enabled = False
        self.index = 0
        self.cmdSet = 0
        self.p1Set = 0
        self.p2Set = 0
        print('Sequence Stopped')
    
    def update(self):
        if(self.index > self.length-2):
            self.enabled = False
            self.index = 0
            print('Sequence Ended')
            self.cmdSet = 0
            self.p1Set = 0
            self.p2Set = 0
        if (self.enabled):
            currentTime = time.time()
            self.tElapsed = currentTime-self.startTime
            while(self.tElapsed > self.times[self.index]):
                self.index += 1
            self.speedSet = self.speeds[self.index]
            self.cmdSet = self.cmds[self.index]
            self.voltageSet = self.voltages[self.index]
            self.flagSet = self.flag[self.index]
            self.p1Set= self.p1[self.index]
            self.p2Set = self.p2[self.index]
            #print(self.tElapsed, self.speedSet, self.cmdSet, self.voltageSet)
            #self.index += 1
