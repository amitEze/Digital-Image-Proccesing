
import cv2
import numpy as np
from scipy import signal
from scipy import misc

from HelperFunctions import filter2D




# imgPath = input("Enter a Picture Path")
imgPath = 'CuteTiger.jpg'


# Read the original image
img = cv2.imread(imgPath) 

gray = cv2.imread(imgPath,flags=0)




# Display original image
cv2.imshow('Original', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

#Choosing Mode
mode=input("Choose mode between \n 1)edge2 detection \n 2)smoothing : ")
if mode=='2':
    #Choosing kernel size:
    kerSize=int(input("Enter the kernel size from 3,5,7,9"))    
    kernel = np.ones((kerSize,kerSize))
    output = signal.convolve2d(img,kernel)
    output = output/np.sum(kernel)
    cv2.imwrite('smoothed_img.jpg')
    cv2.imshow('smoothed',output)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    
    kerX=np.array([[-1, 0 ,1],
                    [-2, 0, 2],
                    [-1, 0, 1]])

    kerY=np.array([[1, 2, 1],
                    [0, 0, 0],
                    [-1, -2, -1]])
    # test_x_wise=signal.convolve2d(gray,kerX,"same")
    # test_y_wise=signal.convolve2d(gray,kerY,"same")
    # test_filter = np.sqrt(test_x_wise*test_x_wise+test_y_wise*test_y_wise)
    # sovel = cv2.Sobel(gray,cv2.CV_16S,1,1,ksize=3,scale=1,delta=0,borderType=cv2.BORDER_DEFAULT)
    # cv2.imwrite('sobeledPicture.jpg',sovel)
    test_filter2d = filter2D(gray,kerX,kerY)
    cv2.imwrite('test_filter2D.jpg',test_filter2d)
    # cv2.imwrite('test_both_sides.jpg',test_filter)
    # cv2.imwrite('test_x_wise.jpg',test_x_wise)
    # cv2.imwrite('test_y_wise.jpg',test_y_wise)



def rgb2Gray(img):
    return np.dot(img[...,:3],[0.299,0.587,0.114])

    


kerI = np.array([[0,0,0],
                 [0,1,0],
                 [0,0,0]])








# actual_filter=cv2.filter2D(img,ddepth=-1,kernel=kerX)
# cv2.imshow('filtered',actual_filter)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

