import cv2
import numpy as np

img = cv2.imread("(13)morfoloji/klon.jpg", 0)
kernel = np.ones((5, 5), np.uint8)
erosion = cv2.erode(img, kernel, iterations = 3)
dilation = cv2.dilate(img, kernel, iterations = 3)
opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
tophat = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel)

cv2.imshow("Original", img)
# cv2.imshow("Erosion", erosion)
# cv2.imshow("Dilation", dilation)
# cv2.imshow("Opening", opening)
# cv2.imshow("Closing", closing)
# cv2.imshow("Tophat", tophat)

cv2.waitKey(0)
cv2.destroyAllWindows()