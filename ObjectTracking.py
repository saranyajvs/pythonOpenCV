import cv2
import numpy as np

img = cv2.imread('blue.jpg', 1)
hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
cv2.imshow("hsv image", hsv_img)
cv2.waitKey(0)
cv2.destroyWindow("hsv image")

lower_blue = np.array([110, 50, 50])
upper_blue = np.array([130, 252, 255])
mask = cv2.inRange(hsv_img, lower_blue, upper_blue)
cv2.imshow("mask", mask)
result = cv2.bitwise_and(img, img, mask=mask)
cv2.imshow("result", result)
cv2.waitKey(0)
cv2.destroyAllWindows()
