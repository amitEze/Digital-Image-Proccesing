import cv2
# load image as grayscale
img = cv2.imread('result0.jpg', 0)
# convert to binary. Inverted, so you get white symbols on black background
_, thres = cv2.threshold(img, 200, 255, cv2.THRESH_BINARY_INV)
# find contours in the thresholded image (this gives all symbols)
contours, hierarchy = cv2.findContours(
    thres, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
# create a list of the indexes of the contours and their sizes
contour_sizes = []
for index, cnt in enumerate(contours):
    contour_sizes.append([index, cv2.contourArea(cnt)])

# sort the list based on the contour size.
# this changes the order of the elements in the list
contour_sizes.sort(key=lambda x: x[1])
print(len(contour_sizes))

# loop through the list and determine the largest relative distance
indexOfMaxDifference = 0
currentMaxDifference = 0
for i in range(1, len(contour_sizes)):
    sizeDifference = contour_sizes[i][1] / \
        contour_sizes[i-1][1] if contour_sizes[i-1][1] != 0 else 0
    if sizeDifference > currentMaxDifference:
        currentMaxDifference = sizeDifference
        indexOfMaxDifference = i

# loop through the list again, ending (or starting) at the indexOfMaxDifference, to draw the contour
for i in range(0, indexOfMaxDifference):
    cv2.drawContours(img, contours, contour_sizes[i][0], (255), -1)
# display result
cv2.imshow('res', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite('result.jpg', img)
