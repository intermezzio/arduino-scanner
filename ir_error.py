import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

IR_ERROR = 11166.750185583001 # precalculated coefficient
ir_func = lambda x: IR_ERROR/x

ir_data = pd.read_csv("ir_error.csv")
fig, ax = plt.subplots()

ax.plot(ir_data["expected"], ir_data["actual"],
	"r.", label="observed data")

input_values = np.linspace(30,60,300)
ax.plot(input_values, input_values, "k--",
	label="f(x) = x")

ax.set_xlabel("Actual Distance (cm)")
ax.set_ylabel("Distance Reading (cm)")
ax.set_title("Error plot for IR Sensor Readings")

fig.legend(loc="center right")
fig.savefig("ir_error.png")

plt.show()