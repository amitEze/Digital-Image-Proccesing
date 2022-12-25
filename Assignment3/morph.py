import cv2
import numpy as np

# Load the image
img = cv2.imread('test1.jpg')

# Convert the image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply Otsu's thresholding
threshold, binarized = cv2.threshold(
    gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# Define the kernel for morphological transformations
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (4, 4))
kernel2 = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))

# Remove the demarcation lines using erosion, dilation, and opening

# eroded = cv2.erode(binarized, kernel, iterations=1)
# dilated = cv2.dilate(eroded, kernel, iterations=1)

closed = cv2.morphologyEx(binarized, cv2.MORPH_CLOSE, kernel)
erosed = cv2.morphologyEx(closed, cv2.MORPH_ERODE, kernel2)


# Invert the image so that the demarcation lines are black and the rest of the image is white
mask = cv2.bitwise_not(erosed)

# Mask the original image with the inverted image to remove the demarcation lines
result = cv2.bitwise_and(binarized, mask)

# Save the result
cv2.imwrite('result2.jpg', erosed)
