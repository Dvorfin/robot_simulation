#from PIL import ImageGrab
#import os
#import time
import cv2
import numpy as np


def find_mana():
    img = cv2.imread("Piiiiiivo.png")  # картинка, на которой ищем объект
    cv2.imshow("img_2", img)
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # преобразуем её в серуюш
    cv2.imshow("img_3", gray_img)
    template = cv2.imread("Object.png", cv2.IMREAD_GRAYSCALE)  # объект, который преобразуем в серый, и ищем его на gray_grayscale
    w, h = template.shape[::-1]
    #w = w + 100
    #h = h +100
    print (w, h)
    result = cv2.matchTemplate(gray_img, template, cv2.TM_CCOEFF_NORMED)
    print(result)
    qt = []
    loc = np.where(result >= 0.162)
    a = 0
    # рисует прямоугольник вокруг объекта
    for pt in zip(*loc[::-1]):
        if (a == 0):
            a = a + 1
            qt.append(pt[0])
            qt.append(pt[1])
            qt[0] = qt[0]
            qt[1] = qt[1] + 100
        #print(loc)
        #quick = loc
        #print(w, h)
        #print("pt = ", pt)
        cv2.rectangle(img, qt, (qt[1] + w, qt[0] + h), (0, 0, 255), 2)

    cv2.imshow("img", img)  # выводит на экран результат
    cv2.imshow("img_1", template)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


def main():
    find_mana()


if __name__ == '__main__':
    main()