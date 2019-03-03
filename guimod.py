#C:\Users\Ben\AppData\Local\Programs\Python\Python37-32\Scripts\pyuic5.exe -x gui.ui -o gui.py
from gui import *
from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import QThread, pyqtSignal, Qt
import pyqtgraph as pg
from sampleFunctions import *
from daq import*
from torqueSensor import*
from dcSensor import*
from absorber import*
from datalogging import*
from roadload import*
from buck import*
from testmotor import*
from sequence import*
import sys
import time
import pandas

tStart = time.time();

ts = .005;

app = QtGui.QApplication(sys.argv)
DynoControlPanel = QtGui.QMainWindow()
ui = Ui_DynoControlPanel()
ui.setupUi(DynoControlPanel)
#list(map(ui.speedSlider.valueChanged.connect, [ui.sBox.setValue, ui.speedSlider.value]))
#list(map(ui.sBox.valueChanged.connect, [ui.speedSlider.setValue, ui.sBox.value]))

dynoDaq = daq(0)
torque_sensor = torqueSensor('/dev/ttyUSB4')
dynoAbsorber = absorber('/dev/ttyUSB0')
dclink = dcSensor('/dev/ttyUSB3')
roadload = roadLoad(0, 0, 0)
buckConverter = buck('COM4')
testMotor  = testmotor('COM6')
sequence = Sequence()

buckConverter.setVoltage(0)
time.sleep(.5);

dynoDaq.zero()






ui.c1Box.setEnabled(False)
ui.c2Box.setEnabled(False)
ui.jBox.setEnabled(False)
#ui.speedSlider.setEnabled(False)
ui.sBox.setEnabled(False)
ui.browseButton.setEnabled(False)
ui.startButton.setEnabled(False)
ui.stopButton.setEnabled(False)
ui.csvEdit.setEnabled(False)
    
tVec = [0]

def loadCSV(filename):
    try:
        print(filename)
        profileData = pandas.read_csv(filename)
        print("loaded some data");
        profileTime = profileData.ix[:,0]
        profileTestCMD = profileData.ix[:,1]
        profileSpeed = profileData.ix[:,2]
        profileVoltage = profileData.ix[:,3]
        profileFlag = profileData.ix[:,4]
        profileP1 = profileData.ix[:,5]
        profileP2 = profileData.ix[:,6]

        sequence.times = profileTime
        sequence.speeds = profileSpeed
        sequence.cmds = profileTestCMD
        sequence.voltages = profileVoltage
        sequence.flag = profileFlag
        sequence.cmdType = 'can'
        sequence.p1 = profileP1
        sequence.p2 = profileP2
        
        
    except:
        print('Invalid CSV')
        return False
    return True

def selectFile():
    file_filter = "CSV (*.csv)"
    filename = QtGui.QFileDialog.getOpenFileName(filter=file_filter)
    filename = filename[0]
    if(filename!=""):
        if(loadCSV(filename)):
            ui.csvEdit.setText(filename)
            ui.startButton.setEnabled(True)
            ui.stopButton.setEnabled(True)
            
def startSequence():
    sequence.start()
    
def stopSequence():
    sequence.stop()
        
        
def setBuckVoltage():
    v = ui.buckBox.value()
    buckConverter.setVoltage(v)
    
def setAbsorberSpeed():
    s = ui.sBox.value()
    dynoAbsorber.setSpeed(s)

def setTestMotorPeriod():
    period = ui.periodBox.value()
    testMotor.setPeriod(period)
    
def setTestMotorPeriodLim():
    pmin = ui.periodMinBox.value()
    pmax = ui.periodMaxBox.value()
    ui.periodBox.setMaximum(pmax)
    ui.periodBox.setMinimum(pmin)
    ui.periodMinBox.setMaximum(pmax)
    ui.periodMaxBox.setMinimum(pmin)
    
def setTestMotorVoltage():
    voltage = ui.testVSetBox.value()
    testMotor.setVoltage(voltage)
    
def setTestMotorVoltageLim():
    vmin = ui.testVMinBox.value()
    vmax = ui.testVMaxBox.value()
    ui.testVSetBox.setMaximum(vmax)
    ui.testVSetBox.setMinimum(vmin)  
    ui.testVMinBox.setMaximum(vmax)
    ui.testVMaxBox.setMinimum(vmin)
    
def setTestMotorCAN():
    torque = ui.canBox.value()
    testMotor.setCANCmd(torque, 0, 0)

def setTestMotorCANLim():
    tmin = ui.canMinBox.value()
    tmax = ui.canMaxBox.value()
    ui.canBox.setMaximum(tmax)
    ui.canBox.setMinimum(tmin)
    ui.canMinBox.setMaximum(tmax)
    ui.canMaxBox.setMinimum(tmin)
     
def roadLoadUpdate():
    roadload.j = ui.jBox.value()
    roadload.c1 = ui.c1Box.value()
    roadload.c2 = ui.c2Box.value()
    t = dynoDaq.Torque
    vel = dynoAbsorber.speedcmd
    if (vel>0):
        c3 = 1
    else:
        c3 = -1
    tnet = t - c3*roadload.c1 - roadload.c2*vel;
    acc = tnet/roadload.j
    newVel = vel+ ts*acc
    if (newVel>600):
        newVel = 600
    elif (newVel<-600):
        newVel = -600
    return (newVel)

def enableTMControls():
    ui.testVMinBox.setEnabled(True)
    ui.testVMaxBox.setEnabled(True)
    ui.testVSetBox.setEnabled(True)
    ui.periodMinBox.setEnabled(True)
    ui.periodMaxBox.setEnabled(True)
    ui.periodBox.setEnabled(True)
    ui.canMinBox.setEnabled(True)
    ui.canMaxBox.setEnabled(True)
    ui.canBox.setEnabled(True)

def disableTMControls():
    ui.testVMinBox.setEnabled(False)
    ui.testVMaxBox.setEnabled(False)
    ui.testVSetBox.setEnabled(False)
    ui.periodMinBox.setEnabled(False)
    ui.periodMaxBox.setEnabled(False)
    ui.periodBox.setEnabled(False)
    ui.canMinBox.setEnabled(False)
    ui.canMaxBox.setEnabled(False)
    ui.canBox.setEnabled(False)
    
def enableRLControls():
    ui.jBox.setEnabled(True)
    ui.c1Box.setEnabled(True)
    ui.c2Box.setEnabled(True)
    
def disableRLControls():
    ui.jBox.setEnabled(False)
    ui.c1Box.setEnabled(False)
    ui.c2Box.setEnabled(False)

def enableMSControls():
   # ui.speedSlider.setEnabled(True)
    dynoAbsorber.enterSpeedMode()
    ui.sBox.setEnabled(True)


def disableMSControls():
    #ui.speedSlider.setEnabled(False)
    ui.sBox.setEnabled(False)

def enableProfileControls():
    ui.browseButton.setEnabled(True)
    ui.csvEdit.setEnabled(True)
    ui.startButton.setEnabled(True)
    ui.stopButton.setEnabled(True)

def disableProfileControls():
    ui.browseButton.setEnabled(False)
    ui.csvEdit.setEnabled(False)
    ui.startButton.setEnabled(False)
    ui.stopButton.setEnabled(False)

def enableBuckControls():
    ui.buckBox.setEnabled(True)
    ui.iMaxBox.setEnabled(True)
    
def disableBuckControls():
    ui.buckBox.setEnabled(False)
    ui.iMaxBox.setEnabled(False)

def disableSelected():
	if(ui.disableButton.isChecked()):
	    disableRLControls()
	    disableMSControls()
	    disableProfileControls()
	    enableBuckControls()
	    enableTMControls()
	    dynoAbsorber.disable()
	    ui.sBox.setValue(0)
    

def rlSelected():
    enableRLControls()
    enableBuckControls()
    enableTMControls()
    disableMSControls()
    disableProfileControls()
    #ui.sBox.setValue(0)
    #ui.speedSlider.setValue(0)
    #dynoAbsorber.speedcmd = 0
    
def msSelected():
    enableMSControls()
    enableBuckControls()
    enableTMControls()
    disableRLControls()
    disableProfileControls()
    
def profileSelected():
    enableProfileControls()
    disableRLControls()
    disableMSControls()
    disableTMControls()
    disableBuckControls()
    ui.sBox.setValue(0)
    #ui.speedSlider.setValue(0)
    

def logSelected():
    if ui.logButton.isChecked():
        filename = ui.filenameEdit.text()
        filename = "Logs/" + filename+".csv"
        try:
            global writer, logFile
            logFile = open(filename, "a")
            writer = csv.writer(logFile, delimiter=',')
            print("file opened")
        except:
            print("that's not a file")
    else:
        try:
            logFile.close()
            print("file closed")
        except:
            pass


def updatePlots(plots, xdata, ydata):
    for i in range(len(plots)):
        plots[i].plot(ydata[i], clear=True)
   
def setSpeedRef(ref):
    dynoAbsorber.setSpeed(ref)
    #print(ref)
    
def sendCmd():
    if(ui.disableButton.isChecked()):
        pass
        #dynoAbsorber.disable()
    elif (ui.rlButton.isChecked()):
        setSpeedRef(roadLoadUpdate())
    elif (ui.sButton.isChecked()):
        setSpeedRef(ui.sBox.value())
    elif (ui.profileButton.isChecked()):
        if(sequence.enabled):
            sequence.update()
            setSpeedRef(sequence.speedSet)
            buckConverter.setVoltage(sequence.voltageSet)
            ui.buckBox.setValue(sequence.voltageSet)
            ui.sBox.setValue(sequence.speedSet)
            ui.sBox.setValue(sequence.speedSet)
            if(sequence.cmdType == 'v'):
                testMotor.setVoltage(sequence.cmdSet)
                ui.testVSetBox.setValue(sequence.cmdSet)
            elif(sequence.cmdType == 'dtc'):
                testMotor.setPeriod(sequence.cmdSet)
                ui.periodBox.setValue(sequence.cmdSet)
            elif(sequence.cmdType =='can'):
                testMotor.setCANCmd(sequence.cmdSet, sequence.p1Set, sequence.p2Set)
                ui.canBox.setValue(sequence.cmdSet)
        else:
            pass
            #dynoAbsorber.disable()
        
        
tv = [0]
iv = [0]
vv = [0]
def sampleAll():
    
    tv.append(torque_sensor.Torque)
    iv.append(dclink.Current)
    vv.append(dclink.Voltage)
    #dclink.sample()
    dynoAbsorber.getSpeed()
    currentTime = time.time()-tStart
    tVec.append(currentTime)
    dt = currentTime - tVec[-2]
    #print(dt)
    
    dataVec = [currentTime, torque_sensor.TorqueVec[-1], dynoAbsorber.speedVec[-1], dclink.VoltageVec[-1], dynoDaq.CurrentVec[-1], sequence.p1Set, sequence.p2Set, sequence.flagSet]
    if(ui.logButton.isChecked()):
        writer.writerow(dataVec)
    #dynoAbsorber.getSpeed()
    #setSpeedRef(ui.speedSlider.value())
    #sendCmd()



        
ui.disableButton.setChecked(True)

torquePlot = pg.PlotWidget(title = 'Torque')
speedPlot = pg.PlotWidget(title = 'Speed')
powerPlot = pg.PlotWidget(title = 'Power') #work and electrical?

ui.PlotLayout.addWidget(torquePlot)  # plot goes on right side, spanning 3 rows
ui.PlotLayout.addWidget(speedPlot)
ui.PlotLayout.addWidget(powerPlot)

ui.rlButton.toggled.connect(lambda:rlSelected())
ui.sButton.toggled.connect(lambda:msSelected())
ui.disableButton.toggled.connect(lambda:disableSelected())
ui.profileButton.toggled.connect(lambda:profileSelected())
ui.logButton.toggled.connect(lambda:logSelected())
ui.buckBox.valueChanged.connect(lambda:setBuckVoltage())
ui.browseButton.clicked.connect(lambda:selectFile())
ui.periodBox.valueChanged.connect(lambda:setTestMotorPeriod())
ui.testVSetBox.valueChanged.connect(lambda:setTestMotorVoltage())
ui.testVMaxBox.valueChanged.connect(lambda:setTestMotorVoltageLim())
ui.testVMinBox.valueChanged.connect(lambda:setTestMotorVoltageLim())
ui.periodMaxBox.valueChanged.connect(lambda:setTestMotorPeriodLim())
ui.periodMinBox.valueChanged.connect(lambda:setTestMotorPeriodLim())
ui.sBox.valueChanged.connect(lambda:setAbsorberSpeed())
ui.canBox.valueChanged.connect(lambda:setTestMotorCAN())
ui.canMinBox.valueChanged.connect(lambda:setTestMotorCANLim())
ui.canMaxBox.valueChanged.connect(lambda:setTestMotorCANLim())
ui.startButton.clicked.connect(lambda:startSequence())
ui.stopButton.clicked.connect(lambda:stopSequence())

def refresh():
    #dynoDaq.sampleAll()
    dynoAbsorber.querySpeed()
    torqueVec = tv[-4000:-1]
    speedVec = dynoAbsorber.speedVec[-4000:-1]
    voltageVec = vv[-4000:-1]
    currentVec = iv[-4000:-1]
    ePowerVec = [v*i for v, i in zip(voltageVec, currentVec)]    
    powerVec = [t*s for t, s in zip(torqueVec, speedVec)]
    
    timeVec = tVec[-4000:-1]
    
    torquePlot.plot(timeVec, torqueVec, clear=True)
    speedPlot.plot(timeVec, speedVec, clear=True)
    #powerPlot.plot(timeVec, voltageVec, clear=True)
    
    ep = pg.PlotCurveItem(timeVec, ePowerVec)
    mp = pg.PlotCurveItem(timeVec, powerVec)
    ep.setPen({'color':"FF0"})
    powerPlot.clear()
    powerPlot.addItem(ep, clear=True)
    powerPlot.addItem(mp)
    
    ui.torqueText.setText('%.3f'%(torqueVec[-1]))
    ui.speedText.setText('%.3f'%(speedVec[-1]))
    ui.voltageText.setText('%.3f'%(voltageVec[-1]))
    ui.currentText.setText('%.3f'%(currentVec[-1]))
    ui.mpText.setText('%.3f'%(torqueVec[-1]*speedVec[-1]))
    ui.epText.setText('%.3f'%(currentVec[-1]*voltageVec[-1]))


class DataObj(QtCore.QObject):
    def __init__(self):
        super(DataObj, self).__init__()
    def sample(self):
        torque_sensor.continuousSample()
        #self.signal.emit(motor.data)

class DataObj2(QtCore.QObject):
    def __init__(self):
        super(DataObj2, self).__init__()
    def sample(self):
        dclink.continuousSample()
        #self.signal.emit(motor.data)

class PlotObj(QtCore.QObject):
    def run(self):
        self.sampleTimer = QtCore.QTimer()
        self.sampleTimer.timeout.connect(lambda:self.sample())
        self.sampleTimer.start(50)
    def sample(self):
        refresh()
        #self.signal.emit(motor.data)

#derpThread = DerpThread()
#dataThread  = DataCollectionThread()







#derpThread.start()
#dataThread.start()
#plotThread.start()
    
    #updatePlots([torquePlot, speedPlot, powerPlot], [torqueVec, speedVec , voltageVec])




dataObj = DataObj()
dataThread = QtCore.QThread()
dataObj.moveToThread(dataThread)
#dataObj.sampleTimer.moveToThread(dataThread)
dataThread.started.connect(dataObj.sample)
dataThread.start()

dataObj2 = DataObj2()
dataThread2 = QtCore.QThread()
dataObj2.moveToThread(dataThread2)
#dataObj.sampleTimer.moveToThread(dataThread)
dataThread2.started.connect(dataObj2.sample)
dataThread2.start()

sampleTimer = QtCore.QTimer()
sampleTimer.setTimerType(Qt.PreciseTimer)
sampleTimer.timeout.connect(lambda:sampleAll())
sampleTimer.start(1000.0*ts)

timerThread = QtCore.QThread()
sampleTimer.moveToThread(timerThread)
timerThread.start()

plotTimer = QtCore.QTimer()
plotTimer.timeout.connect(lambda:refresh())
plotTimer.start(50)

'''
plotObj = PlotObj()
plotThread = QtCore.QThread()
plotObj.moveToThread(plotThread)
plotThread.started.connect(plotObj.run)
time.sleep(.2)
plotThread.start()
'''
DynoControlPanel.show()
sys.exit(app.exec_())
