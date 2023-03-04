import cv2


#Resim okuma
img = cv2.imread("(1)image_read_show_save/klon.jpg")

#print(img)

#Pencerenin küçülüp büyümesi için
cv2.namedWindow("Image", cv2.WINDOW_NORMAL) 

#img = cv2.resize(img, (640, 480)) # fotoğrafa boyut vermek

#Resmi gösterir
cv2.imshow("Image", img) 
#Resmi kaydeder
cv2.imwrite("(1)image_read_show_save/klon1.jpg", img) 
#Ekranda belirtilen kadar tutar
cv2.waitKey(0) 
#Tüm pencerelerin kapanması için
cv2.destroyAllWindows() 
