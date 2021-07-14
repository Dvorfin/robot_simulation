import win32gui as win
from PIL import ImageGrab
import numpy as np
import cv2
import time
import paho.mqtt.client as mqtt


mqttBroker = "mqtt.eclipseprojects.io" #работа с брокером
client = mqtt.Client("OpenSus")
client.connect(mqttBroker)
Beer_x=0
Beer_y=0
Rob_x=0
Rob_y=0

time.sleep(0.5)
while True:
   # win.SetForegroundWindow(hwnd)
    hwnd = win.FindWindow(None, r'ROBOT SIMULATION')
    dimensions = win.GetWindowRect(hwnd)
    image = ImageGrab.grab(dimensions)

    opencvImage = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)

    hsv = cv2.cvtColor(opencvImage, cv2.COLOR_BGR2HSV)
    lower_range = np.array([53, 0, 0])
    upper_range = np.array([83, 255, 255])

    l_range = np.array([14, 62, 132])
    u_range = np.array([31, 246, 253])

    mask = cv2.inRange(hsv, lower_range, upper_range)
    musk = cv2.inRange(hsv, l_range, u_range)
    # cv2.imshow("123", musk)

    contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contours1, hierarchy1 = cv2.findContours(musk, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    # print("cnt= ", contours)

    if len(contours) != 0:
        for contour in contours:
            if cv2.contourArea((contour)) > 400:
                x, y, w, h = cv2.boundingRect(contour)
                cv2.rectangle(opencvImage, (x, y), (x + w, y + h), (0, 0, 255), 1)
                # print (w, h)
                print("Координаты бутылки x:", x + 7, "y", y + 15)
                Beer_x= x+w/2
                Beer_y=y+h/2
    cv2.imshow("Image", opencvImage)

    if len(contours1) != 0:
        for contour1 in contours1:
            if cv2.contourArea((contour1)) > 400:
                x1, y1, w1, h1 = cv2.boundingRect(contour1)
                cv2.rectangle(opencvImage, (x1, y1), (x1 + w1, y1 + h1), (0, 255, 0), 2)

                print (w1, h1)
                print("Координаты коробки x:", x1 + 25, "y", y1 + 25)
                Rob_x=x1+w1/2
                Rob_y=y1+h1/2
    cv2.imshow("Image", opencvImage)
    # cv2.imshow("Mask", mask)
    client.publish("Data_x", Beer_x) #Отправляем данные о местоположении бутылки по по х на брокер
    client.publish("Data_y", Beer_y) #Отправляем данные о местоположении бутылки по у на брокер
    client.publish("Rob_x", Rob_x)  # Отправляем данные о местоположении робота  по х на брокер
    client.publish("Rob_y", Rob_y)  # Отправляем данные о местоположении робота по у на брокер
    time.sleep(0.5)


    if cv2.waitKey(10) == 27:
        break



cv2.waitKey(0)
cv2.destroyAllWindows()