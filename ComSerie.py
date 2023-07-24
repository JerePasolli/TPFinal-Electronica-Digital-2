import serial

ser = serial.Serial('COM9', 9600, timeout=1) 

i = 1

while True:
    try:
        data = ser.readline()
        if data:
            data = int.from_bytes(data)
            voltage = 5*data/1023
            temperature = voltage*100
            print(f"Valor recibido en la habitacion {i}: {round(temperature)}°C")
            if temperature > 22:
                print(f"Aire acondicionado de la habitacion {i} encendido")
            i += 1
            if i == 4:
                i = 1

    except KeyboardInterrupt:
        break

ser.close()
