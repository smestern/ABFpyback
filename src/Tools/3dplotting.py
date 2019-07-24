import pyabf
import pyabf.plot
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import tkinter as tk
from tkinter import filedialog
from mpl_toolkits import mplot3d

root = tk.Tk()
root.withdraw()

file_path = filedialog.askopenfilename()


abf = pyabf.ABF(file_path)


# use a custom colormap to create a different color for every sweep
cm = plt.get_cmap("Set1") 
colors = [cm(x/abf.sweepCount) for x in abf.sweepList]
sweepsNumbers = [1, 4, 5] #declares the sweeps we want to see
xupplim = 2
i = 1
fig = plt.figure(figsize=(10, 6))
ax = plt.axes(projection='3d')

for sweepNumber in sweepsNumbers:
    abf.setSweep(sweepNumber) 
    i1, i2 = 0, int(abf.dataRate * xupplim) #Plots the first 2 seconds of the sweep
    dataX = abf.sweepX[i1:i2] #fills the axis with the time code
    dataY =np.empty(int(abf.dataRate * xupplim)) #since the y axis represents the sweep number, it needs to be a numpy array with the same dimensions as the other arrays. So we create a empty array
    dataY.fill(i) #next we fill it with the plot order. Which remains consistent per sweep.
    dataZ = abf.sweepY[i1:i2] #finally we plot the 'y' values as the z values since z axis traditionally 'up'
    i += 1
    ax.plot3D(dataX, dataY, dataZ, color=colors[sweepNumber], alpha=1)

plt.yticks(np.arange(1, len(sweepsNumbers) + 1, 1)) #technically the yvalue is the order of plotting however, we want to label them based on the sweep number
ax.set_yticklabels(sweepsNumbers) #so we fill the labels of the yvalue with the sweep numbers
plt.xlabel(abf.sweepLabelX)
ax.set_zlabel(abf.sweepLabelY)
plt.ylabel('Sweep Number')


plt.show()
