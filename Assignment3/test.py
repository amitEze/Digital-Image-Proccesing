import cv2
import numpy as np

# Load the image
img = cv2.imread('test1.jpg')

# Convert the image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply Otsu's thresholding
threshold, binarized = cv2.threshold(
    gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# Find all the contours in the image
contours, _ = cv2.findContours(
    binarized, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
mask = np.zeros_like(img)

# Loop through all the contours
for contour in contours:
    # Draw the contour on the image
    cv2.drawContours(mask, [contour], 0, (0, 0, 255), 2)

# Save the result
cv2.imwrite('result.jpg', mask)
