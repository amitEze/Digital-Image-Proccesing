import numpy as np
from scipy import signal
from scipy import misc
import cv2
from HelperFunctions import calc_sobel_kernel

kerX = np.array([[2, 0, 2],
                 [4, 0, 5],
                 [1, 0, 10]])

#print(kerX*kerX)

print(calc_sobel_kernel((3,3)))
