import cycle, os, re
from pylab import *
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as colors


class DataSet:
	def __init__(self, directory):
		files = []
		for file in os.listdir(directory):
			if ".DTA" in file:
				files.append(directory + file)
		files = sorted(files, key=lambda f: int(re.search("(?:#)(.*)(?=\.DTA)", f).group(1)))
		self.data = list(map(lambda x: cycle.Cycle(x), files))

	def plot_point(self, attr):

		for line in attr:
			y = []
			for cycle in self.data:
				y.append(float(cycle.table[line][4]))

			x = np.arange(0, len(y), 1)
			y = np.array(y)
			plt.plot(x, y)

		plt.legend(attr, loc='upper left')
		plt.show()

	def getBackground(self, start=0, end=10):
		points = []
		for cycle in self.data:
			for i in range(start, end):
				points.append(float(cycle.table[i][4]))
		return sum(points) / len(points)

	def plot_spectra(self, attr):
		
		bg =  self.getBackground()
		print ("Background found to be: " + str(bg))
		z = []
		for cycle in self.data:
			col = []
			for row in cycle.table:
				col.append(float(row[attr]) - bg)
			z.append(col)

		y = list(map(lambda y: float(y[3]), self.data[0].table))
		
		X = np.arange(0, len(self.data), 1)
		
		Y = np.array(y)

		X, Y = np.meshgrid(X, Y)


		
		Z = np.array(z)
		Z = np.transpose(Z)
	
		z_min, z_max = Z.min(), np.abs(Z).max()

		# z_std = np.std(Z)
		# z_min, z_max = np.average(Z) - (z_std * 2), np.average(Z) + (z_std * 2)

		# Z = Z + -(Z.min()) + 1

		# print (Z.min()) 

		plt.subplot(1, 1, 1)
		plt.pcolormesh(X, Y, Z)
		plt.axis([X.min(), X.max(), Y.min(), Y.max()])

		plt.colorbar()
		plt.show()


