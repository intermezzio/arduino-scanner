import serial

arduino_com_port = "/dev/ttyACM0"

baud_rate = 115200

serial_port = serial.Serial(arduino_com_port, baud_rate, timeout=1)

with open("points.csv", "w") as outfile:
	outfile.write("x,y,z\n")

while True:
	data = serial_port.readline().decode()

	if len(data):
		distance, x_angle, y_angle, x_pos, y_pos, z_pos = [float(x) for x in data.split()]

		with open("points.csv", "a") as outfile:
			outfile.write(f"{x_pos},{y_pos},{z_pos}\n")
