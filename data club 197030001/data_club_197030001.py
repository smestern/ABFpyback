import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import pyabf
from matplotlib.animation import FFMpegWriter
import time
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()

file_path = filedialog.askopenfilename()


abf = pyabf.ABF(file_path)
#plt.figure(figsize=(10, 8))
plt.ion()

cm = plt.get_cmap("Set1")
colors = [cm(x/abf.sweepCount * 1.25) for x in abf.sweepList]
#plt.gca().axis('on') # hide axes to enhance floating effect
#plt.autoscale(False)
#plt.xlim(0, 3)
#plt.ylim(-100, 50)

sweepNumber=0

abf.setSweep(sweepNumber)

i1, i2 = 0, 1 # plot part of the sweep
dataX = abf.sweepX[i1:i2] # + .25 * sweepNumber
dataY = abf.sweepY[i1:i2]  # + 100 * sweepNumber

framestodisplay = int((abf.dataPointsPerMs * 3000) / 100)
print(abf.dataPointsPerMs)
print(abf.dataRate)
fig, ax = plt.subplots()
xdata, ydata = [], []
ln, = plt.plot(abf.sweepX[i1:i2], abf.sweepY[i1:i2], 'b-')
lstframe = 0
plt.pause(1)
plt.ylabel(abf.sweepLabelY)
plt.xlabel(abf.sweepLabelX)

def init():
    ax.set_xlim(0, 3)
    ax.set_ylim(-100, 50)
    return ln,

def update(i):
    global lstframe
    global abf
    global sweepNumber
    i1, i2 = 0, (i * 100)
    if i >= (framestodisplay - 1):
        print(i2)
        print (i)
        print(abf.sweepPointCount)
        i1,i2 = 0, 0
        
        i = 0
        if sweepNumber < (abf.sweepCount - 1):
            sweepNumber += 1
            abf.setSweep(sweepNumber)
            print(sweepNumber)
        else:
            sweepNumber = 0
            abf.setSweep(sweepNumber)
            print(sweepNumber)
      
    
    ln.set_data(abf.sweepX[i1:i2], abf.sweepY[i1:i2])
    ln.set_color(colors[sweepNumber])
    lstframe = i2
   # print(ani.frame_seq)
    return ln,



ani = animation.FuncAnimation(
    fig, update, init_func=init, frames=framestodisplay, interval=0.001, blit=True, save_count=50)
lstframe = 0

print(ani.frame_seq)


plt.show()

#writer = FFMpegWriter(fps=15, metadata=dict(artist='Me'), bitrate=1800)
#ani.save("movie.mp4")
plt.pause(1000)
#for sweepNumber in abf.sweepList:
#        plt.Figure.clear
#        if (sweepNumber <= 7 & sweepNumber > 1):
 #           abf.setSweep(sweepNumber + 1)
  #          j = 0
   #         k = abf.sweepPointCount
    #        while j <= k:
     #               plt.pause(0.001)
      #              print(j)
       #             print("of")
        #            print(k)
         #           i1, i2 = 0, j # plot part of the sweep
          #          dataX = abf.sweepX[i1:i2] # + .25 * sweepNumber
           #         dataY = abf.sweepY[i1:i2]  # + 100 * sweepNumber
            #        plt.plot(dataX, dataY, color=colors[sweepNumber], alpha=.5)
             #       j += int(k * 0.10)



