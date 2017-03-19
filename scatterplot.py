import sys
import os
import getopt

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import gaussian_kde


################  Comand-line arguments ################
line_skip=0

if len(sys.argv[1:])<=1:  ### Indicates that there are insufficient number of command-line arguments
    print "Warning! wrong command, please read the mannual in Readme.txt."
    print "Example: python scatterplot.py --input input_filename --skip 1 --output output_filename"
else:
    options, remainder = getopt.getopt(sys.argv[1:],'', ['input=',
                                                         'skip=',
                                                         'colormap=',
                                                         'output='])
    for opt, arg in options:
        if opt == '--input': input_file=arg
        elif opt == '--output':output_file=arg
        elif opt == '--skip': line_skip=int(arg)
        elif opt == '--colormap':colormap=arg
        else:
            print "Warning! Command-line argument: %s not recognized. Exiting..." % opt; sys.exit()

handle=open(input_file,'r')

x=[]
y=[]
for i in range(0,line_skip):
    handle.readline()

for line in handle:
    row=line.strip().split("\t")
    x.append(float(row[0]))
    y.append(float(row[1]))


x=np.array(x)
y=np.array(y)

# Calculate the point density
xy=np.vstack([x,y])
z=gaussian_kde(xy)(xy)

# Sort the points by density, so that the densest points are plotted last
idx = z.argsort()
x, y, z = x[idx], y[idx], z[idx]

fig, ax = plt.subplots()  ###plt.subplots() is a function that returns a tuple containing a figure and axes object(s). Thus when using fig, ax = plt.subplots() you unpack this tuple into the variables fig and ax. Having fig is useful if you want to change figure-level attributes or save the figure as an image file later.

ax.scatter(x, y, c=z, cmap=colormap,s=30, edgecolor='')
ax.set_xlim(min(x),max(x))
ax.set_ylim(min(y),max(y))
plt.savefig(output_file)
plt.show()



