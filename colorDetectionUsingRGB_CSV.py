import cv2
import numpy as np
import pandas as pd

index=["color","color_name","hex","R","G","B"]
csv = pd.read_csv('colors.csv', names=index, header=None)

cap = cv2.VideoCapture(0)

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

while True:
    _,frame = cap.read()
    height,width, _ = frame.shape

    cx = int(width/2)
    cy = int(height/2)

    pixel_center = frame[cy,cx]
    b,g,r = int(pixel_center[0]), int(pixel_center[1]), int(pixel_center[2])
    print(pixel_center)
    cv2.circle(frame,(cx,cy),3, (255,255,255), 2)

    def getColorName(R, G, B):
        minimum = 10000
        for i in range(len(csv)):
            d = abs(R - int(csv.loc[i, "R"])) + abs(G - int(csv.loc[i, "G"])) + abs(B - int(csv.loc[i, "B"]))
            if (d <= minimum):
                minimum = d
                cname = csv.loc[i, "color_name"]
        return cname


    text = getColorName(r, g, b) + ' R=' + str(r) + ' G=' + str(g) + ' B=' + str(b)

    cv2.rectangle(frame,(20,40), (cx+100, 80),(b,g,r),-1)
    cv2.putText(frame,text,(30,70),0,0.8,(255,255,255),2,cv2.LINE_AA)

    if (r + g + b >= 600):
        cv2.putText(frame, text, (30, 70), 2, 0.8, (0, 0, 0), 2, cv2.LINE_AA)

    cv2.imshow("frame", frame)

    key = cv2.waitKey(1)
    if key == 27:
        break
cap.release()
cv2.destroyAllWindows()