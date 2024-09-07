import serial
import time

# Configuração da porta serial
serial_arduino = serial.Serial('COM3', 9600)  # Substitua 'COM3' pela porta correta

def ler_dados_sensor():
    serial_arduino.write(b'R')  # Envia comando para ler dados do sensor
    time.sleep(1)
    dados = serial_arduino.readline().decode('utf-8').strip()
    return float(dados)

while True:
    peso = ler_dados_sensor()
    print(f"Peso atual: {peso} kg")
    time.sleep(5)  # Lê os dados a cada 5 segundos

