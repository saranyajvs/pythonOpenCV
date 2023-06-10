import cv2

img = cv2.imread('dress.jpg', 1)
cv2.imshow("image",img)
cv2.waitKey(5000)
cv2.destroyAllWindows()
