import cv2

img = cv2.imread('dress.jpg', 1)
cv2.line(img,(0,0),(400,400),(256,0,0),5)
cv2.rectangle(img,(0,0),(400,400),(0,255,0),5)
cv2.circle(img,(200,200),50,(0,0,255),1) # -1 for filled circle
font=cv2.FONT_HERSHEY_COMPLEX
cv2.putText(img,"Dress",(100,100),font,4,(234,255,167))
cv2.imshow("image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()