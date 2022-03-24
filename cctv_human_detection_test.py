import cv2
import time

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
time.sleep(3) #warming up
if not cap.isOpened():
  exit()

body_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_upperbody.xml')

while True:
    ret, image = cap.read()

    if not ret:
        break

    bodies = body_cascade.detectMultiScale(image)
    for body in bodies:
        (x, y, w, h) = body
        x1, y1, x2, y2 = x, y, x + w, y + h
        cv2.rectangle(image, (x1, y1), (x2, y2), (0, 0, 255), thickness=2)

    cv2.imshow('image', image)

    if cv2.waitKey(1) == ord('q'):
        break

    

cap.release()
cv2.destroyAllWindows()