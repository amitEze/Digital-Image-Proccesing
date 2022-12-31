import cv2
import numpy as np
# load image as grayscale
img = cv2.imread('Example0.jpg', 0)

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

# loop through the list and determine the largest relative distance
indexOfMaxDifference = 0
currentMaxDifference = 0
for i in range(1, len(contour_sizes)):
    sizeDifference = contour_sizes[i][1] / \
        contour_sizes[i-1][1] if contour_sizes[i-1][1] != 0 else 0
    if sizeDifference > currentMaxDifference:
        currentMaxDifference = sizeDifference
        indexOfMaxDifference = i
        biggest_punc = contours[contour_sizes[i-1][0]]

mask = img.copy()
# biggest punctuation
cv2.drawContours(
    mask, contours, contour_sizes[indexOfMaxDifference-1][0], (150), -1)
x, y, w, h = cv2.boundingRect(biggest_punc)

top_left = (y, x)
bottom_right = (y+h, x+w)

# draw bounding rect
cv2.rectangle(mask, (top_left[1], top_left[0]),
              (bottom_right[1], bottom_right[0]), color=150, thickness=3)

# get vertical kernel size of biggest punctuation
minSeq_vertical = h

for x in range(top_left[1], bottom_right[1]+1):
    counter = 0
    for y in range(top_left[0], bottom_right[0]+1):
        while thres[y][x]:
            counter += 1
            y += 1
        if counter > 0:
            minSeq_vertical = min(minSeq_vertical, counter)

# get horizontal kernel size of biggest punctuation
minSeq_horizontal = w

for y in range(top_left[0], bottom_right[0]+1):
    counter = 0
    for x in range(top_left[1], bottom_right[1]+1):
        while thres[y][x]:
            counter += 1
            x += 1
        if counter > 0:
            minSeq_horizontal = min(minSeq_horizontal, counter)

kerSize = max(minSeq_horizontal, minSeq_vertical)+3


print(f'vertical: {minSeq_vertical}, horizontal: {minSeq_horizontal}')


# cv2.imshow('mask', mask)
# cv2.waitKey(0)
# x, y, w, h = cv2.boundingRect(biggest_punc)
cv2.imshow('tresh', thres)
cv2.waitKey(0)
cv2.destroyAllWindows()

print(f'w: {w}, h: {h}')

# Define the kernel for morphological transformations
# kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (kerSize, kerSize))
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5,5))

erosed = cv2.morphologyEx(thres, cv2.MORPH_ERODE, kernel)
dialated = cv2.morphologyEx(erosed, cv2.MORPH_DILATE, kernel)

# loop through the list again, ending (or starting) at the indexOfMaxDifference, to draw the contour
# for i in range(0, indexOfMaxDifference):
#     cv2.drawContours(img, contours, contour_sizes[i][0], (255), -1)
# display result


cv2.imshow('erosed', erosed)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imshow('dialated', dialated)
cv2.waitKey(0)
cv2.destroyAllWindows()

result = cv2.bitwise_not(dialated)
cv2.imshow('result', result)
cv2.waitKey(0)
cv2.destroyAllWindows()


cv2.imwrite('result.jpg', result)
