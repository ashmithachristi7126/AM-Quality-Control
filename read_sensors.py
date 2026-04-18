import serial
import json

ser = serial.Serial("COM7",115200)  # change COM port

while True:

    line = ser.readline().decode().strip()

    try:
        data = json.loads(line)

        temperature = data["temperature"]
        vibration = data["vibration"]
        load = data["load"]
        rpm = data["rpm"]
        distance = data["distance"]

        print("Temperature:",temperature)
        print("Vibration:",vibration)
        print("Load:",load)
        print("RPM:",rpm)
        print("Layer Distance:",distance)

    except:
        pass