from abfderivative import *
import matplotlib.pyplot as plt
import pyabf
from pyabf import filter
import numpy

plt.figure(figsize=(12, 8))


plt.autoscale(True)
plt.xlim(1, 1.5)

abf = pyabf.ABF('19712000.abf')
x, y = derivative(abf, 16, 10)
plot = []
tmpln, = plt.plot(x, y, 'b', color='green', label='PRE-PGE2 cell 1')




plt.axvspan(1.15, 1.25, color='r', alpha=.02, lw=0)
plt.axvline(1.15, 0, 1, color='r', ls='--', alpha = 0.1)
plt.figtext(0.32, 0.855, 'Muscimol (200ms)' , size='13', weight='bold', color='r', alpha=0.5)
plt.grid(alpha=.1)
plt.ylabel('d/dx')
plt.xlabel(abf.sweepLabelX)
plt.title("d/dx of Gaba Current (clamped at -40mv)")
plot.append(tmpln)
abf = pyabf.ABF('19712002.abf')
x, y = derivative(abf, 19, 10)
plot = []
tmpln, = plt.plot(x, y, 'b', color='red', label='POST-PGE2 cell 1')
print(integrate(abf, 19, 19,1, 1.15, 1.5))
plot.append(tmpln)
abf = pyabf.ABF('19709026.abf')
x, y = derivative(abf, 12, 10)
plot = []
tmpln, = plt.plot(x, y, 'b', color='blue', label='PRE-PGE2 cell 2')


#abf = pyabf.ABF('19718000.abf')
#x, y = doublederivative(abf, 30, 10)
#plot = []
#tmpln, = plt.plot(x, y, 'b', color='magenta', label='PRE-PGE2 cell 3')
sin = x, y

print(integrate(abf, 12, 19,1, 1.15, 1.5))

plot.append(tmpln)
plt.legend(fontsize=16)
plt.show()