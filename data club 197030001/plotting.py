import pyabf
import pyabf.plot

import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()

file_path = filedialog.askopenfilename()


abf = pyabf.ABF(file_path)
pyabf.plot.sweeps(abf, title=False, 
    offsetXsec=.1, offsetYunits=20, startAtSec=0, endAtSec=1.5)
pyabf.plot.scalebar(abf, hideFrame=True)
plt.tight_layout()
plt.show()