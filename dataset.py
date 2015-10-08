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

	def plot_voltage(self, voltmin, voltmax, inc=1):
		bg = self.getBackground()
		voltages, im = self.data[0].get_col_data()
		voltages = np.array(voltages)
		print (voltages)
		v_indexs = np.where(voltages >= voltmin and voltages <= voltmax)

		for point in range(v_indexs[0], v_indexs[-1], inc):
			time, data = self.data[point].get_col_data()
			plt.plot(time, data[v_indexs])
		plt.legend(points, loc='upper left')
		plt.show()


	def plot_point(self, attr):
		bg = self.getBackground()
		for line in attr:
			y = []
			for cycle in self.data:
				y.append(float(cycle.table[line][4]) - bg[line])

			x = np.arange(0, len(y), 1)
			y = np.array(y)
			plt.plot(x, y)

		plt.legend(attr, loc='upper left')
		plt.show()

	def plotVerticals(self, points):
		for point in points:
			time, data = self.data[point].get_col_data(self.getBackground())
			plt.plot(time, data)
		plt.legend(points, loc='upper left')
		plt.show()

	def getBackground(self, start=0, end=10):
		points = []
		for point in range(len(self.data[0].table)):
			s = 0
			for cycle in range(start, end):
				s += float(self.data[cycle].table[point][4])
			points.append(s / (end - start))
		return points

	def plot_spectra(self, attr):
		
		bg =  self.getBackground()
		
		z = []
		for cycle in self.data:
			col = []
			for row in range(len(cycle.table)):
				col.append(float(cycle.table[row][attr]) - bg[row])
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
		plt.pcolormesh(X, Y, Z, vmin=Z.min(), vmax=0.8e-8)
		plt.axis([X.min(), X.max(), Y.min(), Y.max()])

		plt.colorbar()
		plt.show()


