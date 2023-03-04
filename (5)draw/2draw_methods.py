import cv2
import numpy as np

canvas = np.zeros((512, 512, 3), dtype=np.uint8) + 255
# cv2.imshow("Canvas", canvas)
# cv2.waitKey(0)
#print(canvas)

#Çizgi
cv2.line(canvas,(50, 50), (512, 512), (255, 0, 255), thickness=5)
cv2.line(canvas,(100, 150), (512, 512), (255, 0, 50), 3)

#Dikdörtgen
#Kalınlık parametresi - olursa içi dolu dikdörtgen oluşur
cv2.rectangle(canvas,(200, 200), (300, 300), (0, 255, 50), 3)
cv2.rectangle(canvas,(250, 250), (275, 275), (25, 100, 50), -1)

#Çember, daire(-1 ile)
cv2.circle(canvas, (250, 250), 100, (100, 155, 50), 3)

#Ucgen 
p1 = (100, 200)
p2 = (50, 50)
p3 = (300, 200)
cv2.line(canvas, p1, p2, (0, 0, 0), 4)
cv2.line(canvas, p2, p3, (0, 0, 0), 4)
cv2.line(canvas, p3, p1, (0, 0, 0), 4)

#Yamuk
points = np.array([[[110, 200], [330, 200], [290, 220], [100, 100]]], np.int32)
#İçi dolu -> True verilir
cv2.polylines(canvas, [points], True, (0, 0, 100), 5)

#Elips
cv2.ellipse(canvas, (400,450), (80, 20), 10, 90, 360, (255, 255, 0), -1)

#Boyut ayarı için
cv2.namedWindow("Canvas", cv2.WINDOW_NORMAL)

cv2.imshow("Canvas", canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()