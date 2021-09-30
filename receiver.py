import serial

arduino_com_port = "/dev/ttyACM0"

baud_rate = 115200

serial_port = serial.Serial(arduino_com_port, baud_rate, timeout=1)

with open("points.csv", "w") as outfile:
	outfile.write("x,y,z\n")

<<<<<<< HEAD
with open("points.csv", "a") as outfile:
	while True:
		data = serialPort.readline().decode()
=======
while True:
	data = serial_port.readline().decode()
>>>>>>> f5a2c1ca4bee9adb53c19d90dd2b2d1e0b26a957

	if len(data):
		distance, x_angle, y_angle, x_pos, y_pos, z_pos = [float(x) for x in data.split()]

		with open("points.csv", "a") as outfile:
			outfile.write(f"{x_pos},{y_pos},{z_pos}\n")
