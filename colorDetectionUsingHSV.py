import cv2

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

while True:
    _,frame = cap.read()
    height,width,_ = frame.shape
    hsv_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    cx = int(width/2)
    cy = int(height/2)

    #Picking pixel center
    pixel_center= hsv_frame[cy,cx]

    hue_value = pixel_center[0]
    s_value = pixel_center[1]
    v_value = pixel_center[2]

    color ="Undefined"

    #RED
    if hue_value <4 :
        if v_value <15:
            color ="BLACK"
        elif v_value > 244 & s_value<7:
            color ="WHITE"
        else:
            color = "RED"

    #ORANGE
    elif hue_value < 18:
        if v_value <15:
            color ="BLACK"
        elif v_value > 244 & s_value < 7:
            color = "WHITE"
        else:
            color = "ORANGE"

    #YELLOW
    elif hue_value < 34:
        if v_value <15:
            color ="BLACK"
        elif v_value > 244 & s_value<7:
            color ="WHITE"
        else:
            color = "YELLOW"

    #GREEN
    elif hue_value < 68:
        if v_value <15:
            color ="BLACK"
        elif v_value > 244 & s_value<7:
            color ="WHITE"
        else:
            color = "GREEN"

    #CYAN
    elif hue_value < 92:
        if v_value <15:
            color ="BLACK"
        elif v_value > 244 & s_value<7:
            color ="WHITE"
        else:
            color = "CYAN"

    #BLUE
    elif hue_value < 126:
        if v_value <15:
            color ="BLACK"
        elif v_value > 244 & s_value<7:
            color ="WHITE"
        else:
            color = "BLUE"

    #VIOLET
    elif hue_value < 145:
        if v_value <15:
            color ="BLACK"
        elif v_value > 244 & s_value<7:
            color ="WHITE"
        else:
            color = "VIOLET"

    #PINK
    elif hue_value < 170:
        if v_value <15:
            color ="BLACK"
        elif v_value > 244 & s_value<7:
            color ="WHITE"
        else:
            color = "PINK"

    else:
        if v_value < 15:
            color = "BLACK"
        elif v_value > 244 & s_value < 7:
            color = "WHITE"
        else:
            color = "RED"

    pixel_center_bgr = frame[cy,cx]
    b,g,r = int(pixel_center_bgr[0]), int(pixel_center_bgr[1]), int(pixel_center_bgr[2])

    cv2.circle(frame, (cx,cy),5, (255,255,255), 3)
    cv2.rectangle(frame, (cx-220, 40), (900, 90), (b,g,r), -1)
    if (r+g+b>=600):
        cv2.putText(frame, color, (cx-50, 77), 3, 1, (0, 0, 0), 2,cv2.LINE_AA)
    else:
        cv2.putText(frame, color, (cx-50,77),3,1, (255,255,255), 2,cv2.LINE_AA)

    cv2.imshow("frame", frame)
    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()
