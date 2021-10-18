import json
import time
import paho.mqtt.client as mqtt
from datetime import datetime

# from config import Config


# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {str(rc)}")

    # Subscribing in on_connect() means that if we lose the connection and reconnect then subscriptions will be renewed.
    client.subscribe('AITHOUSES/AITHOYSA1/ENTOLES/projector')


# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    topic = msg.topic
    print(f"data received from topic: {topic}")

    m_decode = str(msg.payload.decode("utf-8", "ignore"))
    print(f"data type: {type(m_decode)}")
    print(f"data decoded: {m_decode}")

    #print("Converting from Json to Object...")
    #m_in = json.loads(m_decode)
    #print(f"converted data type: {type(m_in)}")
    #print(f"converted data: {m_in}")
    print('\n')


# The callback for when a PUBLISH message is sent to the server.
def on_publish(client, userdata, mid):
    print(f"data published with message id: {mid}")
    print('\n')


if __name__ == '__main__':
    MQTT_HOST = "192.168.1.2"
    MQTT_PORT = 1883
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message
    client.on_publish = on_publish

    client.connect(host=MQTT_HOST, port=MQTT_PORT, keepalive=60)
    client.loop_start()

    run = True
    while run:
        # publishes every 15 seconds
        time.sleep(15)

        payload = json.dumps(
            {
                "keba": {
                    "StationID": "1",
                    "milliAmpere": "6100",
                    "startTimeStamp": str(datetime.utcnow()),
                },
            }
        )

        client.publish('test/keba/1', payload=payload, qos=0, retain=True)

    client.loop_stop()
    client.disconnect()
