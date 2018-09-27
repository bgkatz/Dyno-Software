from gui import *


def disableSelected():
    ui.c1Box.setEnabled(False)
    ui.c2Box.setEnabled(False)
    ui.jBox.setEnabled(False)
    ui.speedSlider.setEnabled(False)
    ui.sBox.setEnabled(False)


def rlSelected():
    ui.c1Box.setEnabled(True)
    ui.c2Box.setEnabled(True)
    ui.jBox.setEnabled(True)
    ui.speedSlider.setEnabled(False)
    ui.sBox.setEnabled(False)

def msSelected():
    ui.c1Box.setEnabled(False)
    ui.c2Box.setEnabled(False)
    ui.jBox.setEnabled(False)
    ui.speedSlider.setEnabled(True)
    ui.sBox.setEnabled(True)

def emSelected():
    pass