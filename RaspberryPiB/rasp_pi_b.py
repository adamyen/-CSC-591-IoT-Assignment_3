from paho.mqtt import client as mqtt_client
from gpiozero import LED

BROKER = '192.168.0.179'
PORT = 1883
MQTT_TOPICS = ['LightStatus', 'Status/RaspberryPiA', 'Status/RaspberryPiC']

LED_LIGHT_STATUS = LED(17)
LED_STATUS_PI_A = LED(23)
LED_STATUS_PI_C = LED(13)

client = mqtt_client.Client('RaspberryPiB')

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to MQTT Broker!")
        for topic in MQTT_TOPICS:
            client.subscribe(topic)
    else:
        print("Failed to connect, return code %d\n", rc)

def on_message(client, userdata, msg):
    print("Message received-> " + msg.topic + " " + str(msg.payload))
    if msg.topic == MQTT_TOPICS[0]:
        light_action = 1 if msg.payload == 'TurnOn' else 0
        switch_light(LED_LIGHT_STATUS, light_action)
    else:
        light_action = 1 if msg.payload == 'online' else 0
        if msg.topic == MQTT_TOPICS[1]:
            switch_light(LED_STATUS_PI_A, light_action)
        else:
            switch_light(LED_STATUS_PI_C, light_action)

def switch_light(led, action):
    if action == 0:
        led.off()
    else:
        led.on()

def run():
    client.connect(BROKER, PORT)
    client.on_connect = on_connect
    client.on_message = on_message
    client.loop_forever()

if __name__ == '__main__':
    try:
        run()
    except KeyboardInterrupt:
        client.loop_stop()
