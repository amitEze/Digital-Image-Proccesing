import cv2
import numpy as np
from HelperFunctions import filter2D, smoothFilter2D, calc_sobel_kernel


# imgPath = input("Enter a Picture Path")
imgPath = 'CuteBuilding.jpg'

# Read the original image
img = cv2.imread(imgPath, 0)

# Display original image
cv2.imshow('Original', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
img = np.float64(img)


# Choosing Mode
mode = input(
    "Choose number for mode between \n 1)edge detection \n 2)smoothing\n")

# Choosing kernel size:
kerSize = int(input("Enter the kernel size from 3,5,7,9 : "))

img = cv2.copyMakeBorder(img, 0, kerSize//2, 0, kerSize//2,
                         borderType=cv2.BORDER_CONSTANT, value=0)

# smoothing
if mode == '2':
    kernel = np.ones((kerSize, kerSize))
    kernel = kernel/np.sum(kernel)
    output = smoothFilter2D(img, kernel)

    cv2.imwrite('smoothed_img.jpg', output)
    output = np.uint8(output)
    cv2.imshow('smoothed', output)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Edge detection
elif mode == '1':
    threshold = int(input(
        "Please choose option number:\n1)no threshold\n2)threshold 100\n3)threshold 200\n"))
    if threshold not in [1, 2, 3]:
        print("You chose Wrong!")

    # calculate kernels
    kerX, kerY = calc_sobel_kernel((kerSize, kerSize))

    # convolution edge detection
    edge_detection_image = filter2D(img, kerX, kerY, threshold)

    cv2.imwrite('edge_detection_image.jpg', edge_detection_image)
    edge_detection_image = edge_detection_image.astype(np.uint8)
    cv2.imshow('Sobel Edge Detection', edge_detection_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

else:
    print("Wrong Value")
