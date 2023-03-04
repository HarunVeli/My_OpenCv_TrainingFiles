import cv2

# img = cv2.imread("(17)contour/contour1.png")
img = cv2.imread("(17)contour/100TL.png")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # Siyah beyaza çevirmemiz gerekiyor bu methodları kullanabilmek için
_, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

contours, _  = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
# print(counters)
cv2.drawContours(img, contours, -1, (0, 0, 255), 3)


cv2.imshow("Counter",img)
cv2.waitKey(0)
cv2.destroyAllWindows()