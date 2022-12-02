import numpy as np
from scipy import signal
from scipy import misc


mat = np.full((3,3), 2)
ker = np.dot(np.identity(3),1/9)

print(mat)
print(ker)
print(signal.convolve2d(mat,ker,"same"))