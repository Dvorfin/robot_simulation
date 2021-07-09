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

    mask = cv2.inRange(hsv, lower_range, upper_range)

    contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # print("cnt= ", contours)

    if len(contours) != 0:
        for contour in contours:
            if cv2.contourArea((contour)) > 40:
                x, y, w, h = cv2.boundingRect(contour)
                cv2.rectangle(opencvImage, (x, y), (x + w, y + h), (0, 0, 255), 1)
                # print(w, h)
                print("Координаты бутылки x:", x + w/2, "y", y + h/2)
                Beer_x = (x+w/2)
                Beer_y = (y+h/2)
    cv2.imshow("Image", opencvImage)
    # cv2.imshow("Mask", mask)
    client.publish("Data_x", Beer_x) #Отправляем данные по х на брокер
    client.publish("Data_y", Beer_y) #Отправляем данные по у на брокер
    time.sleep(0.5)


    if cv2.waitKey(10) == 27:
        break



cv2.waitKey(0)
cv2.destroyAllWindows()