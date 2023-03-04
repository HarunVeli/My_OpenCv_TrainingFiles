import cv2
import numpy as np

img = cv2.imread("(11)rotation/klon.jpg", 0)

row, col = img.shape
M = cv2.getRotationMatrix2D([col/2, row/2], 90, 1)
dst = cv2.warpAffine(img, M, (col, row))

cv2.imshow("Klon", img)
cv2.imshow("Matrix", dst)
cv2.waitKey(0)
cv2.destroyAllWindows()