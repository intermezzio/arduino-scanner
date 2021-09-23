import pandas as pd
import time

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

data = pd.read_csv("points.csv")

while True:
	if data.shape[0] >= 4:
		break
	time.sleep(1)

fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")

# while 
ax.plot_trisurf(data["x"], data["y"], data["z"])

plt.show()