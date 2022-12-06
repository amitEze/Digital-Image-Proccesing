import cv2
import numpy as np
from scipy import signal
from scipy import misc

from HelperFunctions import filter2D




# imgPath = input("Enter a Picture Path")
imgPath = 'CuteTiger.jpg'


# Read the original image
img = cv2.imread(imgPath,0)





# Display original image
cv2.imshow('Original', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
img = np.float64(img)

#Choosing Mode
mode=input("Choose mode between \n 1)edge2 detection \n 2)smoothing : ")
if mode=='2':
    #Choosing kernel size:
    kerSize=int(input("Enter the kernel size from 3,5,7,9 : "))    
    kernel = np.ones((kerSize,kerSize))
    kernel = kernel/np.sum(kernel)
    output = signal.convolve2d(img,kernel)
    output = np.uint8(output)
    cv2.imwrite('smoothed_img.jpg',output)
    cv2.imshow('smoothed',output)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    #Edge detection
    kerX=np.array([[-1, 0 ,1],
                    [-2, 0, 2],
                    [-1, 0, 1]],dtype=np.float64)

    kerY=np.array([[1, 2, 1],
                    [0, 0, 0],
                    [-1, -2, -1]],dtype=np.float64)


    test_filter2d = filter2D(img,kerX,kerY)
    test_filter2d = np.uint8(test_filter2d)
    cv2.imshow('Sobel Edge Detection',test_filter2d)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2.imwrite('test_filter2D.jpg',test_filter2d)
