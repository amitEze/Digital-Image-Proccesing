import cv2
import numpy as np
from scipy import signal
from scipy import misc

from HelperFunctions import filter2D, smoothFilter2D




# imgPath = input("Enter a Picture Path")
imgPath = 'CuteBuilding.jpg'


# Read the original image
img = cv2.imread(imgPath,0)





# Display original image
cv2.imshow('Original', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
img = np.float64(img)

#Choosing Mode
mode=input("Choose number for mode between \n 1)edge detection \n 2)smoothing\n")
#Choosing kernel size:
kerSize=int(input("Enter the kernel size from 3,5,7,9 : "))    
if mode=='2':

    kernel = np.ones((kerSize,kerSize))
    kernel = kernel/np.sum(kernel)
    output = smoothFilter2D(img,kernel)
    
    cv2.imwrite('smoothed_img.jpg',output)
    output = np.uint8(output)
    cv2.imshow('smoothed',output)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
elif mode=='1':
    #Edge detection
    threshold = int(input("Please choose option number:\n1)no threshold\n2)threshold 140\n3)threshold 200\n"))
    if threshold not in [1,2,3]:
        print("You chose Wrong!")
    if kerSize==3:
        kerX=np.array([[-1, 0 ,1],
                        [-2, 0, 2],
                        [-1, 0, 1]])

        kerY=np.array([[1, 2, 1],
                        [0, 0, 0],
                        [-1, -2, -1]])
    elif kerSize==5:
        kerX = np.array([[-2, -1, 0 ,1, 2],
                         [-2, -1, 0 ,1, 2],
                        [-4, -2, 0, 2, 4],
                        [-2, -1, 0, 1, 2],
                        [-2, -1, 0 ,1, 2]])

    edge_detection_image = filter2D(img,kerX,kerY,threshold)

    
    cv2.imwrite('edge_detection_image.jpg',edge_detection_image)
    edge_detection_image = edge_detection_image.astype(np.uint8)
    cv2.imshow('Sobel Edge Detection',edge_detection_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

else:
    print("Wrong Value")
