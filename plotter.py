import pandas as pd
import time

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import seaborn as sns

# simple styling
sns.set(style="whitegrid")

# read data
data = pd.read_csv("points.csv")
num_points = 0

# wait until at least one point has been sent
while True:
	if data.shape[0] != 0:
		num_points = data.shape[0]
		break
	print("Not enough points to start plotting")
	time.sleep(1)

# create plot
fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")

# colormap credit to https://stackoverflow.com/a/28604247/12940893
# color points more red if they're closer to the sensor
scat = ax.scatter(data["x"], data["y"], data["z"], facecolors=cm.coolwarm_r(data["y"]/data["y"].max()))

# set axis labels and title
ax.set_xlabel("x distance (cm)")
ax.set_ylabel("y distance (cm)")
ax.set_zlabel("z distance (cm)")

ax.set_title("IR Scan Data")

# set interactive plot for live data
plt.ion()
plt.show()

while True:
	# check for points every second
	data = pd.read_csv("points.csv")
	
	# if there are more points than before
	if num_points != data.shape[0]:
		num_points = data.shape[0]

		# replot points
		ax.clear()
		scat = ax.scatter(data["x"], data["y"], data["z"], facecolors=cm.coolwarm_r(data["y"]/data["y"].max()))

		ax.set_xlabel("x distance (cm)")
		ax.set_ylabel("y distance (cm)")
		ax.set_zlabel("z distance (cm)")

		ax.set_title("IR Scan Data")
		
		plt.pause(1)
		# redraw surface
		fig.canvas.draw()

	time.sleep(1)

plt.ioff()