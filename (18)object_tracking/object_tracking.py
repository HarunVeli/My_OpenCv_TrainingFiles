import cv2
import numpy as np

cap = cv2.VideoCapture("(18)object_tracking/dog.mp4")

while (1):
    ret, frame = cap.read()
    if(ret == False):
        print("Video is over")
        break
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    # beyaz renk taikibi için renk aralığı (renge göre uygun aralık internetten bulunabilir)
    # hsv code for white 
    sensitivity = 15
    lower_white = np.array([0, 0, 255-sensitivity])
    upper_white = np.array([255, sensitivity, 255])

    mask = cv2.inRange(hsv, lower_white, upper_white)
    res = cv2.bitwise_and(frame, frame, mask = mask)

    cv2.imshow("frame", frame)
    cv2.imshow("mask", mask)
    cv2.imshow("Result", res)

    if cv2.waitKey(30) & 0xFF == ord("q"):
        break

cv2.destroyAllWindows()