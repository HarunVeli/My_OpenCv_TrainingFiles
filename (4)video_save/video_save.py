import cv2

# webcamden video alma
# 0 ana webcam input sırasına göre diğer kameralar
cap = cv2.VideoCapture(0)

loop = True

#tek tek gönderilen frame'leri tutan değişken ve kayit yolu

#Farklı kayıt formatları
# 'W', 'M', 'V', '2'
# *'XVID'

#mp4 için -> *'mp4v'
codec = cv2.VideoWriter_fourcc(*'mp4v')
frameRate = 30
resolution = (640,480)
fileName = "(4)video_save/denemeKaydi.mp4"
videoFileOutput = cv2.VideoWriter(fileName, codec, frameRate, resolution)


while loop:
    ret, frame = cap.read()

    #Görüntüyü döndürmek için
    frame = cv2.flip(frame, 1) 
    #Yakalanan kareleri değişkene yazar
    videoFileOutput.write(frame)



    cv2.imshow("Webcam", frame)

    #alınan her kare sonrası bekletme işlemi (ms)
    #q karakterine basılınca döngüyü terk et
    if cv2.waitKey(1) & 0xFF == ord("q"):
        loop = False

videoFileOutput.release()
#işlem çalışırken başka bir şeye izin vermiyor
cap.release()
cv2.destroyAllWindows()
