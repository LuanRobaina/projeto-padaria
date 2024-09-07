import boto3
import json
from datetime import datetime

# Configuração do cliente AWS IoT
client = boto3.client('iot-data', region_name='us-east-1')

def send_to_cloud(weight):
    payload = {
        'timestamp': datetime.now().isoformat(),
        'weight': weight
    }
    response = client.publish(
        topic='padaria/estoque',
        qos=1,
        payload=json.dumps(payload)
    )
    return response

while True:
    weight = read_sensor_data()
    response = send_to_cloud(weight)
    print(f"Dados enviados: {response}")
    time.sleep(5)

