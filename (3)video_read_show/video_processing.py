import cv2

#webcamden video alma
#0 ana webcam input sırasına göre diğer kameralar
cap = cv2.VideoCapture(0)

#dosyadan okuma
#cap = cv2.VideoCapture("(3)video_read_show/antalya.mp4")

loop = True

while loop:
    ret, frame = cap.read()

    #Görüntüyü döndürmek için
    frame = cv2.flip(frame, 1) 
    cv2.imshow("Webcam", frame)

    #alınan her kare sonrası bekletme işlemi (ms)
    #q karakterine basılınca döngüyü terk et
    if cv2.waitKey(40) & 0xFF == ord("q"):
        loop = False

#işlem çalışırken başka bir şeye izin vermiyor
cap.release()
cv2.destroyAllWindows()