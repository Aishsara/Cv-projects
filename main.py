import cv2
from cvzone.HandTrackingModule import HandDetector

cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)
detector = HandDetector(detectionCon=0.8,maxHands=2)
colorR = (255,0,255)
cx , cy, w, h = 100, 100, 200, 200

while True:
    success, img =  cap.read()
    img = cv2.flip(img, 1)
    hands, img = detector.findHands(img, draw=True)
  #  lmlist, _ = detector.findHands(img)

    if hands:
        for hand in hands:   
            lmList = hand["lmList"]
            if lmList:
                cursor = lmList[8]
                # l, _, _ = detector.findDistance(8, 12, img)  # Make sure to handle the returned values properly
                # print(l)
                # if l and l < 30:
                if cx-w//2 < cursor[0] < cx+w//2 and cy-h//2 < cursor[1] < cy+h//2:
                    colorR = (0,255,0)
                    cx=cursor[0]
                    cy=cursor[1]
                else:
                    colorR = (255,0,255)

    cv2.rectangle(img, (cx-w//2,cy-h//2), (cx+w//2,cy+h//2), colorR ,cv2.FILLED)

    cv2.imshow("Image", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):  # Exit the loop when 'q' is pressed
        break

cap.release()
cv2.destroyAllWindows()
