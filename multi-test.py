import cycle, sys, os, re, dataset
import matplotlib.pyplot as plt


POINT = 520
ATTR = 3

if len(sys.argv) < 2:
	print ("Argument list is too short. Specify a larger data set.")
	exit()


d = {1:"Spectragram", 2:"other", 3:"new", 4:"stuff", 5:"here"}
for k,v in d.iteritems():
	print k,v

response = input("Enter an option (1-5): ")

print "Plotting:", d.get(response)



d = dataset.DataSet(sys.argv[1])

if response == 1:
	d.plot_spectra(4)

elif response == 2:
	d.data[30].plot_attribute(4)
	
elif response == 3:
	d.plotVerticals(range(0, 10, 2))
	
elif response == 4:
	d.plot_voltage(-.25, .11, 1)

elif response == 5:
	d.plot_point(range(0,30,5))

else:
	pass

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