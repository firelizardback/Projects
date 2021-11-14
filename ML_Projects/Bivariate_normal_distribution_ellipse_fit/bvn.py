import matplotlib.image as img
import matplotlib.pyplot as plt
import numpy as np

def rgb2gray(rgb):

    r, g, b = rgb[:,:,0], rgb[:,:,1], rgb[:,:,2]
    gray = 0.2989 * r + 0.5870 * g + 0.1140 * b

    return gray


image = img.imread('fig1-1.png')
image2 = rgb2gray(image)
print(image.shape)
plt.imshow(image2)
plt.show()