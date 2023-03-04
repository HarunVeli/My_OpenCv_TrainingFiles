import cv2
import numpy as np

#resim okuma, açma işlemi
img = cv2.imread("(6)basic_operations/klon.jpg")

# resmin büyüklük değerlerini getirir(kaç piksel)
# dimension = img.shape
# print(dimension)


# renk kodunu getirir
# color = img[420, 500]
# print(color)

# pikselin ayrı ayrı renk kodunu getirir
blue = img[420, 500, 0]
green = img[420, 500, 1]
red = img[420, 500, 2]

# aynı işin method hali
blue1 = img.item(420, 500, 0) # getirme
img.itemset((420, 500, 0), 180) # değiştirme
print("Blue :", blue)
print("Green :", blue)
print("Red :", blue)

# manuel renkte verilebilir maviye bu rengi verdik
# img[420, 500, 0] = 250




cv2.namedWindow("Picture", cv2.WINDOW_NORMAL)
cv2.imshow("Picture", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

 

