import cv2

img = cv2.imread("(20)contour_AreaAndEnvironment/contour.png")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # Siyah beyaza çevirmemiz gerekiyor bu methodları kullanabilmek için
_, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

contours, _  = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
# print(contours)

# alan bulmak
cnt = contours[0]
area = cv2.contourArea(cnt)
print(area)
# çevre bulmak
# Şekil kapalı ise True, açık ise False
perimeter = cv2.arcLength(cnt, True)
print(perimeter)

# moments ile alan bulmak
# M = cv2.moments(cnt)
# print(M["m00"])


cv2.imshow("Counter",img)
cv2.waitKey(0)
cv2.destroyAllWindows()