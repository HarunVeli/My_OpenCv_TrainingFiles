import cv2


#En boy oranını dikkate alarak boyutlandırma (aynı en-boy oranında büyültüyor)
def resizeWithAspectRatio(img, width = None, height = None, inter = cv2.INTER_AREA):

    dimension = None
    (h, w) = img.shape[:2] # Resmin boyutuna erişme yükseklik, genişlik

    if width is None and height is None:
        return img

    if width is None:
        r = height / float(h)
        dimension = (int(w*r), height)
    else:
        r = width / float(h)
        dimension = (width, int(h*r))

    return  cv2.resize(img, dimension, interpolation = inter)

#resmin iki katını boyutunu almak
def takeDoubleImage(img):

    (h, w) = img.shape[:2]
    dimension = (int(w*2), int(h*2))

    return cv2.resize(img, dimension, interpolation=cv2.INTER_AREA)




img = cv2.imread("(2)aspect_radio/klon.jpg")
img1 = resizeWithAspectRatio(img, width=None, height=500, inter=cv2.INTER_AREA)
img2 = takeDoubleImage(img)

cv2.imshow("Original", img)
cv2.imshow("Resized", img1)
#cv2.imshow("Double", img2)

cv2.waitKey(0)
cv2.destroyAllWindows()