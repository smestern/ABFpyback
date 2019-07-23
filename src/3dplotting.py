import pyabf
import pyabf.plot
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()

file_path = filedialog.askopenfilename()


abf = pyabf.ABF(file_path)


# use a custom colormap to create a different color for every sweep
cm = plt.get_cmap("winter")
colors = [cm(x/abf.sweepCount) for x in abf.sweepList]
#colors.reverse()
sweepsNumbers = [1, 4, 5, 6, 7, 8]
i = 1
plt.figure(figsize=(10, 6))
for sweepNumber in sweepsNumbers:
    abf.setSweep(sweepNumber)
    
    i1, i2 = 0, int(abf.dataRate * 2)
    dataX = abf.sweepX[i1:i2] + 0.5 * i
    dataY = abf.sweepY[i1:i2] + 30 * i
    i += 1
    plt.plot(dataX, dataY, color=colors[sweepNumber], alpha=.5)

plt.gca().axis('off')
plt.show()
plt.show()
