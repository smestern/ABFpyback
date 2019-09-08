import numpy as np
import matplotlib.pyplot as plt
import pyabf
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()
sweepdsply=7
file_path = filedialog.askopenfilename()



abf = pyabf.ABF(file_path)

plt.figure(figsize=(12, 8))
plt.style.use('ggplot')

plt.autoscale(False)
plt.xlim(0, 2)
plt.ylim(-100, 50)

for sweepNumber in abf.sweepList:
    abf.setSweep(sweepNumber)
    i1, i2 = 0, int(abf.dataRate * 3) # plot part of the sweep
    dataX = abf.sweepX[i1:i2]
    dataY = abf.sweepY[i1:i2]
    if sweepNumber == sweepdsply:
        plt.plot(dataX, dataY, color='b', alpha=0)
    else:
        plt.plot(dataX, dataY, color='', alpha=0.25)


abf.setSweep(sweepdsply)
i1, i2 = 0, int(abf.dataRate * 3) # plot part of the sweep
dataX = abf.sweepX[i1:i2]
dataY = abf.sweepY[i1:i2]
plt.plot(dataX, dataY, color='b', alpha=1)

plt.show()
