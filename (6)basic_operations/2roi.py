# \region of interest --> ilgi alanı

import cv2

img = cv2.imread("(6)basic_operations/klon.jpg")
cv2.namedWindow("Picture", cv2.WINDOW_NORMAL)

dismension = img.shape[:2]
print(dismension)

# sadece kafaya odakalndık
roi = img[30:200, 200:380]
cv2.imshow("Roi", roi)





cv2.imshow("Picture", img)
cv2.waitKey(0)
cv2.destroyAllWindows()