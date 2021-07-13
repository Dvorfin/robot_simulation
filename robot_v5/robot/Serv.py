import paho.mqtt.client as mqtt
import time

Beer_x = 0
Beer_y = 0

def on_message_x(client, userdata, message):
    print("Received message: ", str(message.payload.decode("utf-8")))
    global Beer_x
    Beer_x = message.payload.decode("utf-8")
    Beer_x = float(Beer_x)
    print("Beer_x ", Beer_x)


def on_message_y(client, userdata, message):
    print("Received message: ", str(message.payload.decode("utf-8")))
    global Beer_y
    Beer_y = message.payload.decode("utf-8")
    Beer_y = float(Beer_y)
    print("Beer_y ", Beer_y)


def start_R():
    mqttBroker = "mqtt.eclipseprojects.io"
    client = mqtt.Client("Robot_x")
    client.connect(mqttBroker)
    client.loop_start()
    client.subscribe("Data_x")
    client.on_message = on_message_x

    mqttBroker = "mqtt.eclipseprojects.io"
    client = mqtt.Client("Robot_y")
    client.connect(mqttBroker)
    client.loop_start()
    client.subscribe("Data_y")
    client.on_message = on_message_y
    #time.sleep(3)


def Get_X():
    return Beer_x

def Get_Y():
    return Beer_y





