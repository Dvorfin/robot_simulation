import paho.mqtt.client as mqtt
from random import randrange, uniform
import time

mqttBroker = "mqtt.eclipseprojects.io"
client = mqtt.Client("HMI")
client.connect(mqttBroker)

def publish(msg):
    client.publish("Commands", msg)
    print("Just published " + msg + " to Topic Commands")
    time.sleep(0.1)

def num():
    global i
    i += 1
    client.publish("Commands", i)
