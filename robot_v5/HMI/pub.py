import paho.mqtt.client as mqtt
import time

mqttBroker = "mqtt.eclipseprojects.io"
client = mqtt.Client("HMI")
client.connect(mqttBroker)

i = 0


def publish(msg):
    client.publish("Commands", msg)
    print("Just published " + msg + " to Topic Commands")
    time.sleep(0.1)

def num():
    global i
    i += 1
    client.publish("Commands", i)
