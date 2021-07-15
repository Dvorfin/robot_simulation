#import win32gui as win
#from PIL import ImageGrab
import numpy as np
import cv2
import time
import Pub

Beer_x = 0
Beer_y = 0
Rob_x = 0
Rob_y = 0
CheckPoint_x = 0
CheckPoint_y = 0

cap = cv2.VideoCapture(0)
time.sleep(0.5)
while True:
   # win.SetForegroundWindow(hwnd)
    #hwnd = win.FindWindow(None, r'ROBOT SIMULATION')
    #dimensions = win.GetWindowRect(hwnd)
    #image = ImageGrab.grab(dimensions)
    flag, img = cap.read()


    opencvImage = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)

    hsv = cv2.cvtColor(opencvImage, cv2.COLOR_BGR2HSV)
    #бутылка
    lower_range = np.array([45, 42, 146])
    upper_range = np.array([92, 102, 255])
    #коробка
    l_range = np.array([19, 118, 186])
    u_range = np.array([255, 255, 255])

    lo_range = np.array([0, 0, 198])
    up_range = np.array([255, 35, 255])

    mask = cv2.inRange(hsv, lower_range, upper_range)
    musk = cv2.inRange(hsv, l_range, u_range)
    misk = cv2.inRange(hsv, lo_range, up_range)
    cv2.imshow("123", mask)
    cv2.imshow("124", musk)
    cv2.imshow("125", misk)
    contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contours1, hierarchy1 = cv2.findContours(musk, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contours2, hierarchy1 = cv2.findContours(misk, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    # print("cnt= ", contours)

    if len(contours) != 0:
        for contour in contours:
            if cv2.contourArea((contour)) > 50:
                x, y, w, h = cv2.boundingRect(contour)
                cv2.rectangle(opencvImage, (x, y), (x + w, y + h), (0, 0, 255), 1)
                # print (w, h)
                print("Координаты бутылки x:", (x + 7)*1.32, "y", (y + 15)*1.34)
                Beer_x= (x+w/2)*1.30
                Beer_y= (y+h/2)*1.34
    cv2.imshow("Image", opencvImage)

    if len(contours1) != 0:
        for contour1 in contours1:
            if cv2.contourArea((contour1)) > 400:
                x1, y1, w1, h1 = cv2.boundingRect(contour1)
                cv2.rectangle(opencvImage, (x1, y1), (x1 + w1, y1 + h1), (0, 255, 0), 2)

                #print (w1, h1)
                print("Координаты коробки x:", (x1 + 25)*1.32, "y", (y1 + 25)*1.34)
                Rob_x = (x1+w1/2)*1.30
                Rob_y = (y1+h1/2)*1.34

    if len(contours2) != 0:
        for contour2 in contours2:
            if cv2.contourArea((contour2)) > 500:
                x2, y2, w2, h2 = cv2.boundingRect(contour2)
                cv2.rectangle(opencvImage, (x2, y2), (x2 + w2, y2 + h2), (255, 0, 0), 2)

                #print (w1, h1)
                print("Координаты чекпоинта x:", x2+w2/2, "y", y2 + h2/2)
                CheckPoint_x = (x2+w2/2)*1.30
                CheckPoint_y = (y2+h2/2)*1.34

    cv2.imshow("Image", opencvImage)
    # cv2.imshow("Mask", mask)
    Pub.Publish_Beer_pos(Beer_x, Beer_y)
    Pub.Publish_Rob_pos(Rob_x, Rob_y)
    Pub.Publish_ChekP_pos(CheckPoint_x, CheckPoint_y)


    if cv2.waitKey(10) == 27:
        break



cv2.waitKey(0)
cv2.destroyAllWindows()
