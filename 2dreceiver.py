import serial
import csv
import time
arduino_com_port = "/dev/cu.usbmodem143101"

baud_rate = 9600

serial_port = serial.Serial(arduino_com_port, baud_rate, timeout=1)

with open("2dpoints.csv", "w") as outfile:
	outfile.write("x,y,z\n")

while True:
	time.sleep(1)
	data = serial_port.readline().decode()

	file = open("2dpoints.csv")
	reader = csv.reader(file)
	lines= len(list(reader))

	if len(data):
		distance, x_angle, y_angle, x_pos, y_pos, z_pos = [float(x) for x in data.split()]

		if lines < 18:
			with open("2dpoints.csv", "a") as outfile:
				outfile.write(f"{x_pos},{y_pos},{z_pos}\n")