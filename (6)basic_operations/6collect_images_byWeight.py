import cv2
import numpy as np

circle = np.zeros((512, 512, 3), np.uint8) + 255
# daire oluşturduk tam merkezde
cv2.circle(circle, (256, 256), 60, (255, 0, 0), -1)

# kare oluşturduk tam merkezde
rectangle = np.zeros((512, 512, 3), np.uint8) + 255
cv2.rectangle(rectangle, (150, 150), (350, 350), (0, 0, 255), -1)

# daireyi %70 kareyi %30 ekledik
dst = cv2.addWeighted(circle, 0.7, rectangle, 0.3, 0)

cv2.namedWindow("Circle", cv2.WINDOW_NORMAL)
cv2.imshow("Circle", circle)
cv2.imshow("Rectangle", rectangle)
cv2.imshow("Dst", dst)


cv2.waitKey(0)
cv2.destroyAllWindows()
