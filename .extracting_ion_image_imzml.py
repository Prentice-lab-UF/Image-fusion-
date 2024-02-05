
"""
Code used to extract the mass spectrometry image from imzML file 
"""
import numpy as np
import numpy.matlib
from pyimzml.ImzMLParser import ImzMLParser


# Write the name of the file including the .imzML at the end in '' below next to "filename ="
filename = 'X:/Liang/matlab/12-22-2022 cory 250/12-22-2022 cory 250.imzML'
p = ImzMLParser(filename)

# Enter the m/z of the intensities you want to use (must have at least 2 decimal places for FTICR data)
mz = 369.235

# create list to store intensity values for each pixel
intensity = []

#create dictionary to store the x,y coordinates for each pixel 
coords_dict = {'x':[],
               'y':[]}

#extract the itensity value and coordinates for each pixel and store in list and dictionary 
for idx , (x,y,z) in enumerate(p.coordinates):
    mzA, intA = p.getspectrum(idx)
    
    mz_diff = abs(mzA-mz)
    if any(mz_diff <0.05) :
        intensity.append(float(max(intA[np.where(mz_diff<0.05)])))
    else:
         intensity.append(0)
    coords_dict['x'].append(x)
    coords_dict['y'].append(y)   
unique_x = np.unique(coords_dict['x'])
unique_y = np.unique(coords_dict['y'])
for key in coords_dict:
    coords_dict[key] = np.array(coords_dict[key])
    for i, xy in enumerate(np.unique(coords_dict[key])):
      coords_dict[key][coords_dict[key] == xy] = i

# creating a blank image 
img = np.zeros([max(coords_dict['y'])+1, max(coords_dict['x'])+1])

# inputing the intensity values into the image 
for x,y,c in zip (coords_dict['x'], coords_dict['y'], intensity):
    img[y,x] = c

#save image
np.savetxt('X:/Liang/matlab/12-22-2022 cory 250/IMS.csv',img,fmt='%.4e',delimiter=',')

