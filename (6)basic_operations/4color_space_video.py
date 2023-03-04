import cv2

# cap = cv2.VideoCapture(0)

cap = cv2.VideoCapture("(6)basic_operations/antalya.mp4")


while True:
    ret, frame = cap.read()
    if(ret == False):
        print("Video bitti")
        break

    # videodan alınan karenin renk uzayını değiştirmek
    # frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    frame = cv2.flip(frame, 1) 
    cv2.imshow("Video", frame)

    if cv2.waitKey(30) & 0xFF == ord("q"):
        break


cap.release()
cv2.destroyAllWindows()