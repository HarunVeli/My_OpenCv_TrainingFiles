import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread("(12)thresholding/klon.jpg", 0) # resim gray olmalı

ret, th1 = cv2.threshold(img, 150, 255, cv2.THRESH_BINARY)
# th2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, 11, 2)

cv2.imshow("Klon", img)
cv2.imshow("Klon-th1", th1)
# cv2.imshow("Klon-th2", th2)
cv2.waitKey(0)
cv2.destroyAllWindows()