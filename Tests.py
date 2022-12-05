import numpy as np
from scipy import signal
from scipy import misc
import cv2

kerX=np.array([[-1, 0 ,1],
                    [-2, 0, 2],
                    [-1, 0, 1]])/9

print(kerX)