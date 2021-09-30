import serial
import csv
import time

# set ports and other constants for collecting data
arduino_com_port = "/dev/cu.usbmodem143101"

baud_rate = 9600

serial_port = serial.Serial(arduino_com_port, baud_rate, timeout=1)

# clear existing points.csv file
with open("points.csv", "w") as outfile:
	outfile.write("x,y,z\n")

while True:
	# every second check for serial data
	time.sleep(1)
	data = serial_port.readline().decode()

	# check how many points are already recorded
	file = open("points.csv")
	reader = csv.reader(file)
	lines= len(list(reader))

	# if data has been sent via Serial
	if len(data):
		distance, x_angle, y_angle, x_pos, y_pos, z_pos = [float(x) for x in data.split()]

		# append point iff there aren't too many points already
		if lines < 443:
			with open("points.csv", "a") as outfile:
				outfile.write(f"{x_pos},{y_pos},{z_pos}\n")
