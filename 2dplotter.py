import pandas as pd
import time

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import seaborn as sns

sns.set(style="whitegrid")

data = pd.read_csv("2dpoints.csv")
num_points = 0

# while True:
# 	if data.shape[0] >= 4:
# 		num_points = data.shape[0]
# 		break
# 	print("Not enough points to start plotting")
# 	time.sleep(1)

fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")

# colormap credit to https://stackoverflow.com/a/28604247/12940893
scat = ax.scatter(data["x"], data["y"], data["z"], facecolors=cm.coolwarm_r(data["y"]/data["y"].max()))
# surf = ax.plot_trisurf(data["x"], data["y"], data["z"])
# m = cm.ScalarMappable(cmap=cm.coolwarm_r)
# m.set_array(data["y"])
# cbar = plt.colorbar(m)

ax.set_xlabel("x distance (cm)")
ax.set_ylabel("y distance (cm)")
ax.set_zlabel("z distance (cm)")

ax.set_title("IR Scan Data")

plt.ion()
plt.show()

while True:
	data = pd.read_csv("2dpoints.csv")
	print(data.shape)
	if num_points != data.shape[0]:
		num_points = data.shape[0]

		# replot points
		# surf.set_verts(list(zip(data["x"], data["y"], data["z"])))
		# scat.set_offsets(list(zip(data["x"], data["y"], data["z"])))
		# scat.set_3d_properties(np.c_[data["x"],data["y"]],data["z"].to_numpy())
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
	