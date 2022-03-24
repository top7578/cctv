import cv2
import winsound

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

ret, back = cap.read()
back = cv2.cvtColor(back, cv2.COLOR_BGR2GRAY)

## 가우시안 블러로 노이즈 제거 (모폴로지, 열기, 닫기 연산도 가능)
back = cv2.GaussianBlur(back, (0, 0), 1.0)

while(True):
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # # 노이즈 제거
    gray = cv2.GaussianBlur(gray, (0, 0), 1.0)

    if ret == False:
        continue

    diff = cv2.absdiff(gray, back)
        
    # 차이가 60이상 255(흰색), 30보다 작으면 0(검정색)
    _, diff = cv2.threshold(diff, 60, 255, cv2.THRESH_BINARY)


    # 레이브링을 이용하여 바운딩 박스 표시
    cnt, _, stats, _ = cv2.connectedComponentsWithStats(diff)
    
    check = False
    for i in range(1, cnt):
        x, y, w, h, s = stats[i]
        
        if s < 100:
            continue
            
        cv2.rectangle(frame, (x, y, w, h), (0, 0, 255), 2)
        check = True
        
    if check:
        winsound.Beep(370,100)

    cv2.imshow('frame', frame)
    # cv2.imshow('diff', diff)
    
    if cv2.waitKey(30) == 27:
        break

cap.release()
cv2.destroyAllWindows()