'''
Plot the temporal pattern of public transit (PS) services and Uber pickups (line chart)

Author: Hui Kong
Date: 09/28/2017

'''
import matplotlib.pyplot as plt
import numpy as np
import os, csv

os.chdir(r"C:\Users\Helen\Box Sync\Project_Uber & public transit NYC\Results\Temporal")

#prepare the data, read from csv file
record=csv.reader(file('tem_plot.csv','rb'))
firstline=True
y=[]


for row in record:
    if firstline:
        firstline=False
        continue
    yk=[]
    firstcolumn=True
    for r in row:
        if firstcolumn:
            firstcolumn=False
            continue
        yk.append(float(r))
    y.append(yk)
        
x = np.arange(24*7)
y=np.array(y)

#draw the chart
fig = plt.figure(figsize=(14,4))    #figure size
ax1 = fig.add_subplot(111)
ax3=ax1.twinx()                     #two y axis with different scale (one for PS, one for Uber

#plot the line chart
ax1.plot(x, y[0,:], color='k')      #plot the PS data
plt.xlim((0,24*7-1))        # x axis scale
ax1.set_ylabel('Public Transit', color='k')
ax3.plot(x, y[1,:], color='c')      #plot the Uber data
ax3.set_ylabel('Uber', color='c')
ax3.tick_params('y', colors='c')
plt.ylim((0,20000))         # y axis scale of uber (ax3)
#plt.legend(loc=1)



#x axis 1: the bottom x axis
minor_ticks= np.arange(0, 24*7, 6)          #dot lines (every 6 hours) 
major_ticks= np.arange(0, 24*7+1, 12)       #x axis ticks (midnight & noon)
ax1.set_xticks(minor_ticks,minor=True)
ax1.set_xticks(major_ticks, minor=False)
ax1.xaxis.grid(True,which='minor')          #show the grids for every 6 hours
major_labels=['midnight','noon']*7+['midnight']
ax1.set_xticklabels([],minor=True)          #no tick labels for the grids
ax1.set_xticklabels(major_labels,minor=False)

#x axis 2
ax2 = ax1.twiny()       #define another x axis
minor_labels=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
ax2.xaxis.tick_top()    #this x axis is on the top
minor_ticks= np.arange(12, 24*7, 23)    #ticks of Days
major_ticks= np.arange(0, 24*7, 23)     #solid lines (every day)
ax2.set_xticks(minor_ticks,minor=True)
ax2.set_xticks(major_ticks, minor=False)
ax2.xaxis.grid(True,which='major',linestyle='-')    #show the grids for every day
ax2.set_xticklabels(minor_labels,minor=True)
ax2.set_xticklabels([],minor=False)

plt.tight_layout()      #set the layout to avoid empty on edges

plt.savefig('temporal.png')
