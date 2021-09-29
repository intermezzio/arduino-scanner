import serial
from math import sind, cosd

arduinoComPort = "COM6"

baudRate = 115200

serialPort = serial.Serial(arduinoComPort, baudRate, timeout=1)

with open("points.csv", "w") as outfile:
	outfile.write("x,y,z\n")

with open("points.csv", "a") as outfile:
	while True:
		data = serialPort.readline().decode()

		if len(data):
			distance, x_angle, y_angle, x_pos, y_pos, z_pos = [float(x) for x in data.split()]

			outfile.write(f"{x_pos},{y_pos},{z_pos}\n")
