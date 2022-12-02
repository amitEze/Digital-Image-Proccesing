import cv2
import numpy as np
from scipy import signal
from scipy import misc

# Read the original image
img = cv2.imread('CuteTiger.jpg') 
img = cv2.resize(img, (0,0), fx=0.5, fy=0.5)


# Display original image
cv2.imshow('Original', img)
cv2.waitKey(0)

kerX = np.array([[-1, 0 ,1],
                [-2, 0, 2],
                [-1, 0, 1]])

kerY = np.array([[1, 2, 1],
                [0, 0, 0],
                [-1, -2, -1]])

# kerX = np.full((3,3), 1)
# kerY = np.full((3,3), 1/9)

# kerX = np.identity(3)

def rgb2Gray(img):
    return np.dot(img[...,:3],[0.299,0.587,0.114])

def filter2D(img, kernelX, kernelY):
    kerSize = len(kernelX)
    rows, cols = img.shape[:2]
    
    #creating black img with size of img
    convX = signal.convolve2d(img,kernelX,boundary='symm',mode='same')
    convY = signal.convolve2d(img,kernelY,boundary='symm',mode='same')
    grad = np.sqrt(convX*convX+convY*convY)
    
    return grad

img = rgb2Gray(img)

# grad = signal.convolve2d(img, kerX, boundary='symm',mode='same')
# grad = np.absolute(grad)

grad=filter2D(img,kerX,kerY)

print(grad[20][20])
cv2.imshow('Grad', grad)
cv2.waitKey(0)
cv2.destroyAllWindows()   
