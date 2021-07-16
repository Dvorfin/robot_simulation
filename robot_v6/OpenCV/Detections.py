import cv2
import numpy as np

Beer_pos = [0, 0]
Rob_pos = [0, 0]
CheckPoint_pos = [0, 0]

def Start_cap():
    global cap
    cap = cv2.VideoCapture(0)

def OpenCV_Work():
    global hsv, opencvImage
    flag, img = cap.read()

    opencvImage = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)

    hsv = cv2.cvtColor(opencvImage, cv2.COLOR_BGR2HSV)  # накладывание фильтра hsv



def Coordinates(x, y, w, h):  # Функция перерасчитывающая координаты с веб камеры в pygame
    Coord_x = (x + w / 2) * 1.30
    Coord_y = (y + h / 2) * 1.34
    return (Coord_x, Coord_y)

def Show_result():
    cv2.imshow("Image", opencvImage)

def Beer_Detecting():  # Функция обнаружения бутылки
    # бутылка
    global Beer_pos
    lower_range = np.array([45, 42, 146])
    upper_range = np.array([92, 102, 255])
    mask = cv2.inRange(hsv, lower_range, upper_range)
    contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    if len(contours) != 0:
        for contour in contours:
            if cv2.contourArea((contour)) > 50:
                x, y, w, h = cv2.boundingRect(contour)
                cv2.rectangle(opencvImage, (x, y), (x + w, y + h), (0, 0, 255), 1)
                Beer_pos = Coordinates(x, y, w, h)


def Rob_Detecting():  # Функция обнаружения робота
    # коробка
    global Rob_pos
    l_range = np.array([19, 118, 186])
    u_range = np.array([255, 255, 255])
    musk = cv2.inRange(hsv, l_range, u_range)
    contours1, hierarchy1 = cv2.findContours(musk, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    if len(contours1) != 0:
        for contour1 in contours1:
            if cv2.contourArea((contour1)) > 400:
                x1, y1, w1, h1 = cv2.boundingRect(contour1)
                cv2.rectangle(opencvImage, (x1, y1), (x1 + w1, y1 + h1), (0, 255, 0), 2)
                Rob_pos = Coordinates(x1, y1, w1, h1)


def CheckP_Detecting():  # Функция обнаружения места доставки
    # Чекпоинт
    global CheckPoint_pos
    lo_range = np.array([0, 0, 198])  # диапозон цветов
    up_range = np.array([255, 35, 255])
    misk = cv2.inRange(hsv, lo_range, up_range)
    contours2, hierarchy1 = cv2.findContours(misk, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    if len(contours2) != 0:
        for contour2 in contours2:
            if cv2.contourArea((contour2)) > 500:
                x2, y2, w2, h2 = cv2.boundingRect(contour2)
                cv2.rectangle(opencvImage, (x2, y2), (x2 + w2, y2 + h2), (255, 0, 0), 2)  # отрисовка прямоугольника

                CheckPoint_pos = Coordinates(x2, y2, w2, h2)


  # подключаем веб-камеру