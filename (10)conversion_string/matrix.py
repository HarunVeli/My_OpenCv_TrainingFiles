import cv2
import numpy as np

img = cv2.imread("(10)conversion_string/klon.jpg", 0)

row, col = img.shape[:2]
# dönüşüm dizeyi
M = np.float32([[1, 0, 20], [0, 1, 70]])
dst = cv2.warpAffine(img, M, (row, col))

cv2.imshow("Klon", img)
cv2.imshow("Matrix", dst)
cv2.waitKey(0)
cv2.destroyAllWindows()