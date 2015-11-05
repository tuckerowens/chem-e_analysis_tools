import cycle, sys, os, re, dataset
import matplotlib.pyplot as plt


if len(sys.argv) < 2:
	print ("Specify a larger data set.")
	exit()

response = 0
o = {1:"Spectragram", 2:"IM across a file", 3:"Range of something"}

while response < 1 or response > len(o):
	for k,v in o.iteritems():
		print k,v
	response = input("Enter an option (1-"+str(len(o))+"): ")

print "Plotting:", o.get(response)

d = dataset.DataSet(sys.argv[1])

if response == 1:
	d.plot_spectra(4)

elif response == 2:
	target=input("Select a data point (1-"+str(len(d.data))+"): ")
	d.data[target-1].plot_attribute(4)
	
elif response == 3:
	range_start=input("Start point of range(1-"+str(len(d.data))+"): ")
	range_end=input("End point of range("+str(range_start)+"-"+str(len(d.data))+"): ")
	interval=input("interval: ")
	d.plotVerticals(range(range_start, range_end, interval))
	
else:
	pass