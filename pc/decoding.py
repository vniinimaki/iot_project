'''
A simple script to decode the binary file "photobin.txt" into an image file "image.png".
Used to debug the camera module.
'''


import numpy as np
from PIL import Image

# Define width and height
w, h = 160, 120

# Read file using numpy "fromfile()"
with open('photobin.txt', mode='rb') as f:
    d = np.fromfile(f,dtype=np.uint16,count=w*h).reshape(h,w)
print(str(d.size))
# Make into PIL Image and save
PILimage = Image.fromarray(d)
PILimage.save('image.png')
