# import win32gui as win
# from PIL import ImageGrab
import numpy as np
import cv2
import time
import Pub
import Detections as Det

Det.Start_cap()

time.sleep(0.5)
while True:
    ###         захват изображения с экрана          ###

    # win.SetForegroundWindow(hwnd)
    # hwnd = win.FindWindow(None, r'ROBOT SIMULATION')
    # dimensions = win.GetWindowRect(hwnd)
    # image = ImageGrab.grab(dimensions)

    ###                                             ###

    Det.OpenCV_Work()

    Det.Beer_Detecting()  # вызов функции по поиску бутылки
    Pub.Publish_Beer_pos(Det.Beer_pos[0], Det.Beer_pos[1])  # публикация координат бутылки

    Det.Rob_Detecting()  # вызов функции по поиску робота
    Pub.Publish_Rob_pos(Det.Rob_pos[0], Det.Rob_pos[1])  # публикация координат робота

    Det.CheckP_Detecting()  # вызов функции по поиску чекпоинта
    Pub.Publish_ChekP_pos(Det.CheckPoint_pos[0], Det.CheckPoint_pos[1])  # публикация координат чекпоинта

    Det.Show_result() # отображение результата поиска

    if cv2.waitKey(10) == 27:
        break

cv2.waitKey(0)
cv2.destroyAllWindows()
