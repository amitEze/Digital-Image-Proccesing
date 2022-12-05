import numpy as np


def filter2D(img, kernelX, kernelY):
    kerSize = len(kernelX)
    rows, cols = img.shape[:2]
    grad = np.zeros((rows, cols))

    for y in range((kerSize-1)//2, rows-(kerSize-1)//2):
        for x in range((kerSize-1)//2, cols-(kerSize-1)//2):
            Gx = 0
            Gy = 0
            for i in range(-kerSize//2, (kerSize//2)+1):
                for j in range(-kerSize//2, (kerSize//2)+1):
                    val = img[y+i, x+j]
                    Gx += int(kernelX[kerSize//2+i][kerSize//2+j]) * val
                    Gy += int(kernelY[kerSize//2+i][kerSize//2+j]) * val
            sqrt = int(np.sqrt(Gx*Gx + Gy*Gy))
            if sqrt>255:
                print(sqrt)
            # if sqrt<140:
            #     sqrt = 0
            # else:
            #     sqrt=255
            grad[y,x] = sqrt

    return grad
