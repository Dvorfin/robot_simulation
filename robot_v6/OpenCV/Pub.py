import paho.mqtt.client as mqtt
import time

mqttBroker = "mqtt.eclipseprojects.io" #работа с брокером
client = mqtt.Client("OpenSus")
client.connect(mqttBroker)
Beer_x = 0
Beer_y = 0
Rob_x = 0
Rob_y = 0
CheckPoint_x = 0
CheckPoint_y = 0


def Publish_Beer_pos(x, y):
    client.publish("Data_x", x)  # Отправляем данные о местоположении бутылки по по х на брокер
    client.publish("Data_y", y)  # Отправляем данные о местоположении бутылки по у на брокер
    time.sleep(0.1)

def Publish_Rob_pos(x, y):
    client.publish("Rob_x", x)  # Отправляем данные о местоположении робота  по х на брокер
    client.publish("Rob_y", y)  # Отправляем данные о местоположении робота по у на брокер
    time.sleep(0.1)

def Publish_ChekP_pos(x, y):
    client.publish("CheckPoint_x", x)  # Отправляем данные о местоположении чекпоинта
    client.publish("CheckPoint_y", y)
    time.sleep(0.1)


