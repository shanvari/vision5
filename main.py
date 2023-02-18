import numpy as np
import matplotlib.pyplot as plt
import cv2
from math import floor, ceil, sqrt
import pywt
import skimage

import warnings
warnings.filterwarnings("ignore")

def imshow(*args, figsize=10, title=None, fontsize=12):
    if isinstance(figsize, int):
        figsize = (figsize, figsize)
    images = args[0] if type(args[0]) is list else list(args)
    if title is not None:
        assert len(title) == len(images), "Please provide a title for each image."
    plt.figure(figsize=figsize)
    for i in range(1, len(images)+1):
        plt.subplot(1, len(images), i)
        if title is not None:
            plt.title(title[i-1], fontsize=fontsize)
        plt.imshow(images[i-1], cmap='gray')
        plt.axis('off')
    plt.show()


def normalize(a):
    if isinstance(a, list):
        return list(map(normalize, a))
    if isinstance(a, tuple):
        return tuple(normalize(list(a)))
    return ((a - a.min()) / (a.max() - a.min())) * 255


def gaussian_pyramid(img, num_levels):
    lower = img.copy()
    gaussian_pyr = [lower]
    for i in range(num_levels):
        lower = cv2.pyrDown(lower)
        gaussian_pyr.append(np.float32(lower))
    return gaussian_pyr


def laplacian_pyramid(gaussian_pyr):
    laplacian_top = gaussian_pyr[-1]
    num_levels = len(gaussian_pyr) - 1
    
    laplacian_pyr = [laplacian_top]
    for i in range(num_levels,0,-1):
        size = (gaussian_pyr[i - 1].shape[1], gaussian_pyr[i - 1].shape[0])
        gaussian_expanded = cv2.pyrUp(gaussian_pyr[i], dstsize=size)
        laplacian = np.subtract(gaussian_pyr[i-1], gaussian_expanded)
        laplacian_pyr.append(laplacian)
    return laplacian_pyr

#5.1.1
img = cv2.imread('mona lisa.jpg', cv2.IMREAD_GRAYSCALE)
img = cv2.resize(img, (256, 256)) 

g_pyramid = gaussian_pyramid(img, 4)
imshow(g_pyramid, figsize=14)
 
l_pyramid = laplacian_pyramid(g_pyramid)
imshow(l_pyramid, figsize=14) 


#5.1.4
img = cv2.imread('Lena.bmp', cv2.IMREAD_GRAYSCALE)

 (2, 2, 2)
plt.imshow(# wavelet transform
cA, (cH, cV, cD) = pywt.dwt2(img, 'haar', mode='periodization')

# Plot the results
plt.figure(figsize=(10, 10))
plt.subplot(2, 2, 1)
plt.imshow(cA, cmap='gray')
plt.axis('off')

plt.subplot cH, cmap='gray')
plt.axis('off')

plt.subplot(2, 2, 3)
plt.imshow(cV, cmap='gray')
plt.axis('off')

plt.subplot(2, 2, 4)
plt.imshow(cD, cmap='gray')
plt.axis('off')
plt.show()
 
Multi-level Wavelet Decomposition
We can use pywt.wavedec2() to perform multi-level wavelet decomposition.
C = pywt.wavedec2(img, 'filter_name', mode='mode', level=n)
Where C is the list of coefficients: 
C=[cAn,(cHn,cVn,cDn),(cHn−1,cVn−1,cDn−1),...,(cH1,cV1,cD1)]
And we can access the nth level coefficients in this way:
c_level1 = C[-1]
c_level2 = C[-2]
...
c_leveln = C[-n]
cAn = C[0]
Note: the default value for level is the maximum possible level in decomposition: 
⌊log2(img_lenfilter_len−1)⌋


#5.1.5
img = cv2.imread('Lena.bmp', cv2.IMREAD_GRAYSCALE)

# wavelet transform
coeffs = pywt.wavedec2(img, 'haar', mode='periodization', level=3)

# Put coefficients in a matrix
c_matrix, c_slices = pywt.coeffs_to_array(coeffs)

# Plot
plt.figure(figsize=(12, 12))
plt.imshow(c_matrix, cmap='gray')
plt.axis('off')
plt.show()
