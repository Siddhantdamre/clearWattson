import paho.mqtt.client as mqtt
import time
import random

broker = "your_broker_address"
port = 1883
client = mqtt.Client("WaterMonitor")

def connect_mqtt():
    client.connect(broker, port)
    print("Connected to MQTT Broker")

def publish_data(sensor_data):
    client.publish("water/sensor", sensor_data)

if __name__ == "__main__":
    connect_mqtt()
    while True:
        pH_value = random.uniform(6.5, 7.5)  # Simulated sensor data
        publish_data(f"pH: {pH_value}")
        time.sleep(5)
