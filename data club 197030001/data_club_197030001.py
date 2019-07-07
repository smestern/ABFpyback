
import matplotlib.pyplot as plt
import pyabf
import time

abf = pyabf.ABF("19703008.abf")
plt.figure(figsize=(10, 8))
plt.ion()

cm = plt.get_cmap("Set1")
colors = [cm(x/abf.sweepCount * 1.25) for x in abf.sweepList]
plt.gca().axis('off') # hide axes to enhance floating effect



plt.show()
for sweepNumber in abf.sweepList:
    
        if (sweepNumber <= 7 & sweepNumber > 1):
            abf.setSweep(sweepNumber)
            j = 0
            k = abf.sweepPointCount
            while j <= k:
                    plt.pause(0.001)
                    print(j)
                    i1, i2 = 0, j # plot part of the sweep
                    dataX = abf.sweepX[i1:i2] + .25 * sweepNumber
                    dataY = abf.sweepY[i1:i2] + 100 * sweepNumber
                    plt.plot(dataX, dataY, color=colors[sweepNumber], alpha=.5)
                    j += 1000
      
        
    
plt.ioff()  