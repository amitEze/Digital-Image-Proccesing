import numpy as np
import cv2

def filter2D(img, kernelX, kernelY):
    kerSize = len(kernelX)-1
    print(kerSize)
    rows, cols = img.shape[:2]
    grad = np.zeros((rows, cols), img.dtype)
    for y in range(round((kerSize)/2), round(rows-(kerSize)/2)):
        for x in range(round((kerSize)/2), round(cols-(kerSize)/2)):
            Gx = 0
            Gy = 0
            for i in range(round(-kerSize/2), round(kerSize/2)+1):
                for j in range(round(-kerSize/2), round(kerSize//2)+1):
                    val = img[y+i, x+j]
                    Gx += kernelX[round(kerSize/2)+i][round(kerSize/2)+j] * val
                    Gy += kernelY[round(kerSize/2)+i][round(kerSize/2)+j] * val
            
            sqrt = Gx+Gy
            # if sqrt<100:
            #     sqrt = 0
            # elif sqrt>150:
            #     sqrt = 200
            grad[round(y-kerSize/2),round(x-kerSize/2)] = Gy
    return grad

def smooth_fliter(img,ker):
    kerSize = len(ker)
    rows, cols = img.shape[:2]
