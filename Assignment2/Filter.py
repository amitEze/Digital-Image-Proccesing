import cv2
import numpy as np
from scipy import signal
from scipy import misc



# imgPath = input("Enter a Picture Path")
imgPath = 'CuteTiger.jpg'


# Read the original image
img = cv2.imread(imgPath) 

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)




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
    output = signal.convolve2d(img,kernel,'same')
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
    test_x_wise=signal.convolve2d(gray,kerX,"same")
    test_y_wise=signal.convolve2d(gray,kerY,"same")
    test_filter = np.sqrt(test_x_wise*test_x_wise+test_y_wise*test_y_wise)
    cv2.imwrite('test_both_sides.jpg',test_filter)
    cv2.imwrite('test_x_wise.jpg',test_x_wise)
    cv2.imwrite('test_y_wise.jpg',test_y_wise)



def rgb2Gray(img):
    return np.dot(img[...,:3],[0.299,0.587,0.114])

def filter2D(img, kernelX, kernelY):
    kerSize = len(kernelX)
    print(kernelY[1][0])
    rows, cols = img.shape[:2]
    grad = np.zeros((rows, cols))

    for y in range(kerSize-1//2, rows-kerSize-1//2):
        for x in range(kerSize-1//2, cols-kerSize-1//2):
            Gx = 0
            Gy = 0
            for i in range(-kerSize//2, (kerSize//2)+1):
                for j in range(-kerSize//2, (kerSize//2)+1):
                    val = img[y+i, x+j]
                    Gx += kernelX[i][j] * val
                    Gy += kernelY[i][j] * val

            grad[y - kerSize//2, x - kerSize//2] = int(np.sqrt(Gx*Gx + Gy*Gy))

    return grad
    


kerI = np.array([[0,0,0],
                 [0,1,0],
                 [0,0,0]])








# actual_filter=cv2.filter2D(img,ddepth=-1,kernel=kerX)
# cv2.imshow('filtered',actual_filter)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

