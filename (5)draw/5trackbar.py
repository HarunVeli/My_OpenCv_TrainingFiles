import cv2
import numpy as np


def nothing(x):
    pass


canvas = np.zeros((512, 512, 3), np.uint8) + 255
cv2.namedWindow("image", cv2.WINDOW_NORMAL)

cv2.createTrackbar("R", "image", 0, 255, nothing)
cv2.createTrackbar("G", "image", 0, 255, nothing)
cv2.createTrackbar("B", "image", 0, 255, nothing)
cv2.createTrackbar("Off, On", "image", 0, 1, nothing)

while True:
    cv2.imshow("image", canvas)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

    r = cv2.getTrackbarPos("R", "image")
    g = cv2.getTrackbarPos("G", "image")
    b = cv2.getTrackbarPos("B", "image")
    s = cv2.getTrackbarPos("Off, On", "image")

    if s == 0:
        canvas[:] = [0, 0, 0]
    if s == 1:
        canvas[:] = [b, g, r]

cv2.destroyAllWindows()



