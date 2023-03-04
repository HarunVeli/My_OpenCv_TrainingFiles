import cv2
import numpy as np

canvas = np.zeros((512, 512, 3), dtype=np.uint8) + 255

font = cv2.FONT_HERSHEY_SIMPLEX
font1 = cv2.FONT_HERSHEY_COMPLEX
font2 = cv2.FONT_HERSHEY_SCRIPT_COMPLEX

#girilen koordinat metnin sol altıdır(3.parametre)
cv2.putText(canvas, "Hello World!", (10, 200), font, 4, (0, 0, 0), cv2.LINE_AA)



#Boyut ayarı için
#cv2.namedWindow("Canvas", cv2.WINDOW_NORMAL)

cv2.imshow("Canvas", canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()