import paho.mqtt.client as mqtt
import time

Beer_x = 0
Beer_y = 0
Rob_x = 0
Rob_y = 0

def on_message_x(client, userdata, message): #Прием данных о местоположении бутылки по х
    #print("Received message: ", str(message.payload.decode("utf-8")))
    global Beer_x
    Beer_x = message.payload.decode("utf-8")
    Beer_x = float(Beer_x)
    #print("Beer_x ", Beer_x)

def on_message_y(client, userdata, message): #Прием данных о местоположении бутылки по х
    #print("Received message: ", str(message.payload.decode("utf-8")))
    global Beer_y
    Beer_y = message.payload.decode("utf-8")
    Beer_y = float(Beer_y)
    #print("Beer_y ", Beer_y)

def on_message_Rob_x(client, userdata, message):
    #print("Received message: ", str(message.payload.decode("utf-8")))
    global Rob_x
    Rob_x = message.payload.decode("utf-8")
    Rob_x = float(Rob_x)
    #print("Rob_x ", Rob_x)

def on_message_Rob_y(client, userdata, message):
    #print("Received message: ", str(message.payload.decode("utf-8")))
    global Rob_y
    Rob_y = message.payload.decode("utf-8")
    Rob_y = float(Rob_y)
    #print("Rob_y ", Rob_y)


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

    mqttBroker = "mqtt.eclipseprojects.io"
    client = mqtt.Client("Robot_Rob_x")
    client.connect(mqttBroker)
    client.loop_start()
    client.subscribe("Rob_x")
    client.on_message = on_message_Rob_x

    mqttBroker = "mqtt.eclipseprojects.io"
    client = mqtt.Client("Robot_Rob_y")
    client.connect(mqttBroker)
    client.loop_start()
    client.subscribe("Rob_y")
    client.on_message = on_message_Rob_y

def Get_X():
    return Beer_x

def Get_Y():
    return Beer_y

def Get_Rob_X():
    return Rob_x

def Get_Rob_Y():
    return Rob_y
