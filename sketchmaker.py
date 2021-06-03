import cv2
import sys
#from matplotlib import pyplot as plt
src= input("Enter path : \t")
img_rgb = cv2.imread(src)
img_grey = cv2.cvtColor(img_rgb , cv2.COLOR_BGR2GRAY)

img_grey_inv = 255 - img_grey

img_blur = cv2.GaussianBlur(img_grey_inv , ksize=(21 ,21) , sigmaX=0 , sigmaY = 0)

output = cv2.divide(img_grey , 255-img_blur , scale= 256.0)

#cv2.nameWindow("image" , cv2.WINDOW_AUTOSIZE)
#cv2.nameWindow("pencilsketch" , cv2.WINDOW_AUTOSIZE)

cv2.imshow("image" , img_rgb)
cv2.imshow("pencilsketch" , output)

cv2.waitKey(0)
cv2.destroyAllWindows()
