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
		#print(self.X)
		#print(sum(self.X)/56)
		print("Uncertainty degree: " + str(round(sum(self.X)/56, 3)))


	def wavalength(self):
		# calculate wavalength
		"""self.lamta = list()
		for i in range(0, 8):
			self.lamta.append(round(L[i]/8, 5))							#(2*math.pi)/self.L[i]
			print(1000*self.lamta[i])"""
		self.Aver_lamta = self.Aver_L/8
		print(self.Aver_lamta)
		print()
		#self.Aver_lamta = round(sum(self.lamta)/len(self.lamta), 5)
		print("Wavalength: " + str(self.Aver_lamta))
		self.Y = list()
		"""
		for i in range(0, 8):
			self.Y.append(1000*round((self.lamta[i]-self.Aver_lamta)**2, 8))
		print(self.Y)
		if sum(self.Y) < 0.001:
			print("Uncertainly degree: 0.001")
		else:
			print(sum(self.Y)/56)"""
		for i in range(0, 8):
                    self.Y.append(round((self.L[i]/8-self.Aver_lamta)**2, 5))
        print("Uncertainty degree:  " + str(round((sum(self.Y)/56+0.000001)**0.5, 5)))

	def wavaspeed(self):
		# calculate wavaspeed
		self.Z = list()
		for i in range(0, 8):
			self.Z.append(self.L[i]*37.368)
		print("wavaspeed: " + str(sum(self.Z)/len(self.Z)/8))


#L = [74.64, 75.50, 74.54, 74.82, 74.78, 74.70, 74.70, 74.84]
#L = [72.28, 72.32, 72.72, 72.72, 72.48, 72.64, 72.44, 72.56]
#L = [72.16, 72.40, 72.36, 72.32, 72.20, 72.40, 72.16, 72.40]
#L = [72.38, 72.04, 72.00, 72.06, 72.08, 72.12, 72.12, 72.06]
#L = [74.06, 73.92, 73.80, 74.20, 74.20, 73.88, 73.88, 73.90]
#L = [70.24, 69.70, 69.90, 69.48, 69.4, 69.88, 70.64, 69.5]
L = [72.78, 73.00, 72.88, 72.90, 72.34, 72.40, 72.88, 72.24]
A = tsvm(L)
A.length()
A.wavalength()
A.wavaspeed()
