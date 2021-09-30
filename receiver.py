import serial
import csv
import time

# set ports and other constants for collecting data
ARDUINO_COM_PORT = "/dev/cu.usbmodem143101"
BAUD_RATE = 9600
SERIAL_PORT = serial.Serial(ARDUINO_COM_PORT, BAUD_RATE, timeout=1)
PREFIX = "3d" # can be "2d", "3d", or ""

# clear existing points.csv file
with open(PREFIX + "points.csv", "w") as outfile:
	outfile.write("x,y,z\n")

while True:
	# every second check for serial data
	time.sleep(1)
	data = SERIAL_PORT.readline().decode()

	# check how many points are already recorded
	file = open(PREFIX + "points.csv")
	reader = csv.reader(file)
	lines= len(list(reader))

	# if data has been sent via Serial
	if len(data):
		distance, x_angle, y_angle, x_pos, y_pos, z_pos = [float(x) for x in data.split()]

		# append point iff there aren't too many points already
		if lines < 443:
			with open("points.csv", "a") as outfile:
				outfile.write(f"{x_pos},{y_pos},{z_pos}\n")
