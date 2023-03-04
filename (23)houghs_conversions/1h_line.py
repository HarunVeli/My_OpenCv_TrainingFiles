import cv2
import numpy as np

img = cv2.imread("(23)houghs_conversions/h_line.png")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray, 75, 150)

# cv2.HoughLines()
# MaxLİneGap ile bulunan çizgi sayısını arttırabiliriz fotoğrafa göre değiştirilebilir
lines = cv2.HoughLinesP(edges, 1, np.pi/180, 50, maxLineGap=200)
# print(lines)

for line in lines:
    x1, y1, x2, y2 = line[0]
    cv2.line(img, (x1, y1) ,(x2, y2), (0, 255, 0), 2)


cv2.imshow("Img", img)
cv2.imshow("Gray", gray)
cv2.imshow("Edges", edges)

cv2.waitKey(0)
cv2.destroyAllWindows()
