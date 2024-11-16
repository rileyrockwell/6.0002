class Drunk:
	def __init__(self, a, b):
		self.a = a
		self.b = b

class PolarBearDrunk(Drunk):
	def takeStep(self):
		directionList = [(0.0, 0.5), (1.0, 0.0), (-1.0, 0.0), (0.0, 1.5)]



instance = PolarBearDrunk(0, 0)
print(instance.takeStep())