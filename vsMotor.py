

from motor import MotorControlBoard
from scb import ServoControlBoard


class vsServo():
	def __init__(self):
		self.current = 0;
		self.temp = 0;
		#self.current_ref = 0;
		try:
			self.mcb = MotorControlBoard()
			self.scb = ServoControlBoard()
			self.mcb.set_power(True)
			print('connected to vsServo')
		except:
			print('failed to connect to vsServo')
			pass

	def read_temp(self):
		self.temp = self.scb.get_present_temperature()

	def read_current(self):
		self.current = self.scb.get_present_torque()

	def set_torque(self, current_ref):
		self.scb.set_goal_torque(current_ref)
		