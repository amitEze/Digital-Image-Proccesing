import numpy as np
import cv2

def smoothFilter2D(img, kernelX):
    kerSize = len(kernelX)-1
    rows, cols = img.shape[:2]
    grad = np.zeros((rows, cols))
    for y in range(round((kerSize)/2), round(rows-(kerSize)/2)):
        for x in range(round((kerSize)/2), round(cols-(kerSize)/2)):
            Gx = 0
            Gy = 0
            for i in range(round(-kerSize/2), round(kerSize/2)+1):
                for j in range(round(-kerSize/2), round(kerSize//2)+1):
                    val = img[y+i, x+j]
                    Gx += kernelX[round(kerSize/2)+i][round(kerSize/2)+j] * val
            
            # if sqrt<100:
            #     sqrt = 0
            # elif sqrt>150:
            #     sqrt = 200
            grad[round(y-kerSize/2),round(x-kerSize/2)] = Gx
    return grad

def filter2D(img, kernelX, kernelY, threshold):
    kerSize = len(kernelX)-1
    rows, cols = img.shape[:2]
    grad = np.zeros((rows, cols))
    for y in range(round((kerSize)/2), round(rows-(kerSize)/2)):
        for x in range(round((kerSize)/2), round(cols-(kerSize)/2)):
            Gx = 0
            Gy = 0
            for i in range(round(-kerSize/2), round(kerSize/2)+1):
                for j in range(round(-kerSize/2), round(kerSize//2)+1):
                    val = img[y+i, x+j]
                    Gx += kernelX[round(kerSize/2)+i][round(kerSize/2)+j] * val
                    Gy += kernelY[round(kerSize/2)+i][round(kerSize/2)+j] * val
            
            calc = np.sqrt(Gx*Gx+Gy*Gy)
            
            #Thresholding
            
            if threshold==2:
                if calc>100:
                    calc=255
                else:
                    calc=0
            elif threshold==3:
                if calc>200:
                    calc=255
                else:
                    calc=0
    
            grad[round(y-kerSize/2),round(x-kerSize/2)] = calc
    return grad

