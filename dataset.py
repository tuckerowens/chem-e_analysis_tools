import cycle, os, re, math
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

	def rms(self, values, width=5, bg=0):
		results = []
		for p in range(width-1, len(values)):
			s = 0
			for i in range(width):
				s += (values[p-i] - bg)**2
			results.append( math.sqrt( (1.0/width) * s ) )
		return results 

	def getRmsBackground(self, deltaThresh, width=5):

		bg = self.getBackground(0, 5)

		points = []
		for point in range(len(self.data[0].table)):
			sub_points = []
			for cycle in range(len(self.data)):
				sub_points.append(float(self.data[cycle].table[point][4]))
			points.append(sub_points)

		background = []
		for point in range(len(points)):
			err = self.rms(points[point], width, bg=bg[point])
			if point % 100 == 0:
				x = np.arange(0, len(err), 1)
				y = np.array(err)
				plt.title("Point " + str(point))
				plt.plot(x, y)
				plt.show()
			start = 0
			for i in range(1, len(err)):
				if abs(err[i] - err[i-1]) >= deltaThresh:
					start = i-1
					break
			background.append( np.average(points[point][start:start+width]) )
		return background







	def plotVerticals(self, points):
		bg = self.getBackground();
		for point in points:
			x, y = self.data[point].get_col_data()
			y = list(map(lambda z: z-bg[point], y))
			plt.plot(x, y)
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

	def plot_spectra(self, rms=0):
		if rms:
			bg =  self.getRmsBackground(1E-8)
		else:
			bg = self.getBackground(0, 5)
		attr = 4
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


