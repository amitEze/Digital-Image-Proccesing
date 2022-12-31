import cv2
import numpy as np




imgPath = 'Example0.jpg'
# img = cv2.imread(imgPath, 0)




#main function
def removePunctuation(imgPath: str, altitude: str):
    #load image
    img = cv2.imread(str(imgPath),0)
    
    #Show original image
    cv2.imshow('original', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    

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

    if altitude=='area':
        #area inelation
        print('area')
        THRESHOLD = 0.085
        max_area = contour_sizes[-1][1]
        
        for cnt in contours:
            if cv2.contourArea(cnt)/max_area<THRESHOLD:
                    cv2.drawContours(img, [cnt], -1, 255, thickness=-1)

    elif altitude=='width and height':
        #width and height inelation
        THRESHOLD = 0.45
        max_width_and_height = cv2.boundingRect(contours[contour_sizes[-1][0]])[2:]
        max_w ,max_h = max_width_and_height[0], max_width_and_height[1]
        for cnt in contours:
            w,h = cv2.boundingRect(cnt)[2:]
            if w<max_w*THRESHOLD and h<max_h*THRESHOLD:
                cv2.drawContours(img, [cnt], -1, 255, thickness=-1)
    
    kerSize = (7,7)
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT,kerSize)
    opening = cv2.morphologyEx(img, cv2.MORPH_OPEN,kernel)           
    
    cv2.imshow('res',opening)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
    cv2.imwrite('result.jpg', opening)
    # return img
    
    
removePunctuation('Example2.jpg','area')
# cv2.imwrite('Result.jpg', res)

