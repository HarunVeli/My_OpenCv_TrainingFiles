import cv2

img = cv2.imread("(19)imageMoments_centroid/contour.png")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # Siyah beyaza çevirmemiz gerekiyor bu methodları kullanabilmek için
_, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
# Ağırlık merkezi bulacağız
M = cv2.moments(thresh)
# print(M)
X = int(M["m10"]/M["m00"])
Y = int(M["m01"]/M["m00"])

cv2.circle(img, (X, Y), 3, (0, 0, 255), -1)

cv2.imshow("Object",img)
cv2.waitKey(0)
cv2.destroyAllWindows()