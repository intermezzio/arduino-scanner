import pandas as pd
import time

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

data = pd.read_csv("points.csv")
num_points = 0

while True:
	if data.shape[0] >= 4:
		num_points = data.shape[0]
		break
	time.sleep(1)

fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")

ax.plot_trisurf(data["x"], data["y"], data["z"])

plt.show() # remove ???

'''
while True:
	data = pd.read_csv("points.csv")
	if num_points < data.shape[0]:
		num_points = data.shape[0]

		# replot points
		ax.set_xdata(data["x"]) ???
		??? y, z ???

		# redraw surface
		ax.draw() ????

'''

