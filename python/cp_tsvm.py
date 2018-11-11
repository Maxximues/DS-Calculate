import math

class tsvm():
	def __init__(self, L):
		self.L = L


	def length(self):
		# calculate length
		self.Aver_L = round(sum(self.L)/len(self.L), 2)
		print("Length: " + str(self.Aver_L))
		self.X = list()
		for i in range(0, 8):
			self.X.append(round((self.L[i]-self.Aver_L)**2, 5))
		print(self.X)
		print(sum(self.X)/56)
		print("Uncertainty degree: " + str(round(sum(self.X)/56, 3)))


	def wavalength(self):
		# calculate wavalength
		self.lamta = list()
		for i in range(0, 8):
			self.lamta.append(round((2*math.pi)/self.L[i], 5))
			print(1000*self.lamta[i])
		print()
		self.Aver_lamta = round(sum(self.lamta)/len(self.lamta), 5)
		print("Wavalength: " + str(1000*self.Aver_lamta))
		self.Y = list()
		for i in range(0, 8):
			self.Y.append(1000*round((self.lamta[i]-self.Aver_lamta)**2, 8))
		print(self.Y)
		if sum(self.Y) < 0.001:
			print("Uncertainly degree: 0.001")
		else:
			print(sum(self.Y)/56)


	def wavaspeed(self):
		# calculate wavaspeed
		self.Z = list()
		for i in range(0, 8):
			self.Z.append(self.L[i]*37.368)
		print("wavaspeed: " + str(sum(self.Z)/len(self.Z)/8))


L = [74.64, 75.50, 74.54, 74.82, 74.78, 74.70, 74.70, 74.84]

A = tsvm(L)
A.length()
A.wavalength()
A.wavaspeed()
