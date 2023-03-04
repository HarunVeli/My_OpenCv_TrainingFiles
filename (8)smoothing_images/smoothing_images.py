import cv2
import numpy as np

img_filter = cv2.imread("(8)smoothing_images/filter.png")
img_median = cv2.imread("(8)smoothing_images/median.png")
img_bilateral = cv2.imread("(8)smoothing_images/bilateral.png")

blur = cv2.blur(img_filter, (5, 5))
blur_g = cv2.GaussianBlur(img_filter, (5, 5), cv2.BORDER_DEFAULT)
blur_m = cv2.medianBlur(img_median, 7)
blur_b = cv2.bilateralFilter(img_bilateral, 9, 75, 75)

# cv2.imshow("Original", img_filter)
cv2.imshow("Blur", blur)
cv2.imshow("Blur1", blur_g)
cv2.imshow("BlurMedian", blur_m)
cv2.imshow("BlurBilateral", blur_b)

cv2.waitKey(0)
cv2.destroyAllWindows()