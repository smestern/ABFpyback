
![preview gif](https://i.imgur.com/Dhe9oM6.gif "preview gif")
# ABFpyback
Python Script to allow 'replay' or live-playback of AXON binary files (.abf) generated by the pCLAMP suite of tools.

This is a rough script and may need some tweaking to get exactly what you desire.

Also included are some side scripts I use to visualize ABF data for presentations.
  
  This includes:
  #### 3dplotting.py
  Inline plotting of sweeps based on sweep numbers. Fully interactive.  
  ![example 3d plot](https://i.imgur.com/pEoVkDb.png "3d plot")
  ### abfderivative.py
  **Note: This functionality is now built into pyABF, and the script is no longer needed**
  Callable functions that provide the derivative, double derivative, and integral of the abf curve. (See: https://github.com/smestern/abfderivative)
  ![example Dx](https://i.imgur.com/snbPCru.png "example dx")
  
  
>Please note that these scripts are not intended for intense statistical analysis of ABF files

### Requirements
-Python 3.6 or higher

-PyABF

-Numpy

-Matplotlib

-ffmpeg (optional for saving as mp4)

### How to
The script should function out of the box.

Simply execute the script in your favourite python enviroment.  
Aside from abfderivative, the scripts are stand alone and have no callable functions (although this may be added in the future).   Documention is provided so that you can customize to get exactly what you desire.
  
  To utilize ffmpeg for export, place ffmpeg.exe must be in the same folder as the python script. 
  
### Todo
 -Full tutorial
 
 -GUI buttons to matplot
 
 -Juypter notebook
  
