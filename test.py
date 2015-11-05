import cycle, sys, os, re, dataset
import matplotlib.pyplot as plt


POINT = 520
ATTR = 3

if len(sys.argv) < 2:
	print ("Too short")
	exit()


d = dataset.DataSet(sys.argv[1])
d.plot_spectra()
# d.plot_spectra(rms=1)

# d.data[30].plot_attribute(4)


# d.plotVerticals(range(0, 10, 2))

# d.plot_voltage(-.25, .11, 1)

d.plot_point(range(0,30,5))

# files = []

# for file in os.listdir(sys.argv[1]):
# 	if ".DTA" in file:
# 		files.append(sys.argv[1] + file)


# files = sorted(files, key=lambda f: int(re.search("(?:#)(.*)(?=\.DTA)", f).group(1)))


# data = map(lambda x: cycle.Cycle(x), files)

# output = []
# time = []
# for cycle in data:
# 	output.append(float(cycle.table[POINT][ATTR]))
# 	time.append(float(cycle.table[POINT][2]))
# 	print cycle.filename


# d.plot_point(500)