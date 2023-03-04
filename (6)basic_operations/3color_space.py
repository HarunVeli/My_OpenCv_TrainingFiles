import cv2
import numpy as np
# foroğrafları sınıflandırmak

img = cv2.imread("(6)basic_operations/klon.jpg")
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow("Picture", img)
cv2.imshow("Rgb", img_rgb)
cv2.imshow("Hsv", img_hsv)
cv2.imshow("Gray", img_gray)


cv2.waitKey(0)
cv2.destroyAllWindows()


