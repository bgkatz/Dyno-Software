import pyvesc
import serial

class Vesc():
	def __init__(self, COM):
		self.current = 0;
		#self.current_ref = 0;
		try:
			self.ser = serial.Serial(COM, timeout = .05)
			self.ser.baudrate = 115200
			print('connected to Vesc')
		except:
			print('failed to connect to Vesc')
			pass

	def set_current(self, current_ref):
		self.ser.write(pyvesc.encode(pyvesc.SetCurrent(int(current_ref))))
		