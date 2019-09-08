import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import pyabf
from pyabf import filter
from matplotlib.animation import FFMpegWriter
import time
import tkinter as tk
from tkinter import filedialog


#Opens file open dialog
root = tk.Tk()
root.withdraw()
file_path = filedialog.askopenfilename()
abf = pyabf.ABF(file_path) #If you would prefer you can change file_path to manually point at a specific file


#### EASY SETTINGS ######
cm = plt.get_cmap("Set3") #Changes colour based on sweep number
colors = [cm(x/abf.sweepCount * 1.5) for x in abf.sweepList]
sweepNumberX=4 #this is the first sweep that is printed, change this if needed
Xsecupperlim = 5 #this is the upper bound of the x axis. try to change this variable and not the others
fps = 30 #FPS Module. Should render properly
speedmult = 1 #New speed multiplier, the higher the number - > slower and vice versa
frameinterval = 1 / (fps / 1000)
plotstep = 10 #The amount of data ploted between points. Increase this number to increase performance
framestodisplay = int(((Xsecupperlim * 1000) + 100) * (1 / frameinterval)) * speedmult #This is the number of frames
pyabf.filter.gaussian(abf, 0, 0) #Removes noise. Essential if you want to plot large amounts of data at once. for one line, you are probably okay setting the 2nd value to 0.
lstframe = (abf.dataPointsPerMs * (frameinterval)) / speedmult
sweepatonce = 5 #number of sweeps to display at once. In testing leave at one for now
displayprev = False #Previously written sweeps remain on the graph
########################

i1, i2 = 0, 1 #defines the number of points. ignore this one

sweepNumber = sweepNumberX

fig, ax = plt.subplots()
if sweepatonce == 1:
    abf.setSweep(sweepNumberX)
    ln, = plt.plot(abf.sweepX[i1:i2:plotstep], abf.sweepY[i1:i2:plotstep], 'b-')
   
else:
    displayprev = False
    ln, = [plt.plot(abf.sweepX[i1:i2:plotstep], abf.sweepY[i1:i2:plotstep], 'b-')]
    #ann = []
    
    for x in range(0, sweepatonce):
        
        abf.setSweep(x)
 
        tmpln, = plt.plot(abf.sweepX[i1:i2:plotstep], abf.sweepY[i1:i2:plotstep], 'b-')
        ln.append(tmpln)
        #tempann = plt.annotate(str(x),xy=(abf.sweepX[i2],abf.sweepY[i2]),fontsize="16")
        #ann.append(tempann)
        

cycles = 0

plt.pause(1)
plt.ylabel(abf.sweepLabelY)
plt.xlabel(abf.sweepLabelX)
fig.set_size_inches(10, 8) #sets the figure size in inches
if displayprev == True:
    iterations = framestodisplay * (abf.sweepCount - 1)
else:
    iterations = framestodisplay
prevln = []
dataX = []
dataY = []


def init():
    global sweepNumber
    global cycles
    global ln
    fig.canvas.draw()
    ax.set_xlim(0, Xsecupperlim)
    ax.set_ylim(-600, 650) #the Y axis limits 
    print('init')
    
    cycles = 1
    
    if sweepatonce > 1:
        ln[0].set_color(colors[sweepNumber])
        return ln
    else:
        ln.set_color(colors[sweepNumber])
        return ln,

def update(i):
    global lstframe, dataX, dataY, abf, sweepNumber, ln, iterations, framestodisplay, cycles, prevln
    
    if cycles > 1:
        frmcount = i - (framestodisplay * (cycles - 1))
        
    else: 
        frmcount = i
    i1, i2 = 0, int(frmcount * lstframe) #This is the data that is drawn. Essentially this mean it prints the line data between 0 (origin) and the frame (i) * 100. So frame one it prints 0 - 100ms, frame 2 is 0 - 200ms
   
    
    if i >= ((framestodisplay * cycles) - 1) and sweepatonce < 2 :
        if sweepNumber < (abf.sweepCount - 1):
            
            if displayprev == True:
                dataX.append(abf.sweepX[i1:i2:plotstep])
                dataY.append(abf.sweepY[i1:i2:plotstep])
                templn, = plt.plot(dataX[cycles - 1], dataY[cycles - 1], "b")
                templn.set_color(colors[sweepNumber])
                print(sweepNumber)
                print(templn)
                prevln.append(templn)
            
            
            sweepNumber += 1
            cycles += 1
            abf.setSweep(sweepNumber)
            i1, i2 = 0, 0
            ln, = plt.plot(abf.sweepX[i1:i2:plotstep], abf.sweepY[i1:i2:plotstep], 'b-')
            ln.set_color(colors[sweepNumber])
            print(sweepNumber)
        else:
            sweepNumber = 0
            abf.setSweep(sweepNumber)
           
            ln, = plt.plot(abf.sweepX[i1:i2:plotstep], abf.sweepY[i1:i2:plotstep], 'b-')
            print(sweepNumber)
        
            
        
    
        
    if sweepatonce > 1:
        for x in range(0, sweepatonce):
            abf.setSweep(x)
            
            
            ln[x].set_data(abf.sweepX[i1:i2:plotstep], abf.sweepY[i1:i2:plotstep])
            
            
            ln[x].set_color(colors[x - 1])
            #ann[x].set_position(xy=(abf.sweepX[i2],abf.sweepY[i2]))
        #return ln + ann
        return ln
    else:   
       
        
        
        ln.set_data(abf.sweepX[i1:i2:plotstep], abf.sweepY[i1:i2:plotstep])
        ln.set_zorder(20)
       
        
        return [ln] + prevln


    
print("frames: " + str(framestodisplay))
print("FramesI:  " + str(iterations))

ani = animation.FuncAnimation(
    fig, update, init_func=init, frames=iterations, interval=frameinterval, blit=True, save_count=1)

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

print(ani.frame_seq)
writer = FFMpegWriter(fps=29, metadata=dict(artist='Me'), bitrate=-1)
#ani.save(file_path + ".mp4")


plt.show()


plt.pause(1000)



