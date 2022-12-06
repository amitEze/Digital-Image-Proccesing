import numpy as np
import cv2

def filter2D(img, kernelX, kernelY):
    kerSize = len(kernelX)-1
    rows, cols = img.shape[:2]
    grad = np.zeros((rows, cols))
    for y in range((kerSize)//2, rows-(kerSize)//2):
        for x in range((kerSize)//2, cols-(kerSize)//2):
            Gx = 0
            Gy = 0
            for i in range(-kerSize//2, (kerSize//2)+1):
                for j in range(-kerSize//2, (kerSize//2)+1):
                    val = img[y+i, x+j]
                    Gx += kernelX[kerSize//2+i][kerSize//2+j] * val
                    Gy += kernelY[kerSize//2+i][kerSize//2+j] * val
            
            sqrt = round(np.sqrt(Gx*Gx + Gy*Gy))
            grad[round(y-kerSize/2),round(x-kerSize/2)] = sqrt
    return grad

def smooth_fliter(img,ker):
    kerSize = len(ker)
    rows, cols = img.shape[:2]
