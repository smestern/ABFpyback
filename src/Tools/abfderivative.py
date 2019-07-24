import numpy as np
import matplotlib.pyplot as plt
import pyabf
from pyabf import filter
import tkinter as tk
from tkinter import filedialog
import random




def derivative(abf, sweepNumber, filter=0):
    abf.setSweep(sweepNumber)
    pyabf.filter.gaussian(abf,filter,0)
    
    dy=np.diff(abf.sweepY,1)
    dx=np.diff(abf.sweepX,1)
    dataY=dy/dx
    dataX = 0.5*(abf.sweepX[:-1]+abf.sweepX[1:])


    return dataX, dataY
    
def doublederivative(abf, sweepNumber, filter=0):
    dataY = []
    i2 = abf.sweepPointCount
    pyabf.filter.gaussian(abf,filter,0)
    abf.setSweep(sweepNumber)
    dy=np.diff(abf.sweepY,1)
    dx=np.diff(abf.sweepX,1)
    dataY=dy/dx
    dataX = 0.5*(abf.sweepX[:-1]+abf.sweepX[1:])
    dyfirst=np.diff(dataY,1)
    dxfirst=np.diff(dataX,1)
    ysecond=dyfirst/dxfirst

    xsecond=0.5*(dataX[:-1]+dataX[1:])
    dataY = ysecond
    dataX = xsecond
    return dataX, dataY


def integrate(abf, sweepNumber, filter=0, step=1, xlwllim=0, xupplim=-1):
   i1, i2 = int(((xlwllim * 1000) * abf.dataPointsPerMs)), int(((xupplim * 1000) * abf.dataPointsPerMs))
   pyabf.filter.gaussian(abf, filter, 0)
   abf.setSweep(sweepNumber)
   x = abf.sweepX[i1:i2]
   y = abf.sweepY[i1:i2]
   
   area = np.trapz(y,x,step)

   return area
