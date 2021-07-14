import paho.mqtt.client as mqtt

foo = 0

def on_message(client, userdata, message):
    print("Received message: ", str(message.payload.decode("utf-8")))
    global foo
    foo = message.payload.decode("utf-8")


def start():
    mqttBroker = "mqtt.eclipseprojects.io"
    client = mqtt.Client("Robot")
    client.connect(mqttBroker)
    client.loop_start()
    client.subscribe("Commands")
    client.on_message = on_message
    #time.sleep(3)

def get_msg():
    return foo




