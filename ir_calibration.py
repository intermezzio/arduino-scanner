import numpy as np
import pandas as pd
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

ir_data = pd.read_csv("ir_calibration.csv")

coeff = curve_fit(lambda x, a: a/x,ir_data["cm"], ir_data["read"])[0][0]
print(coeff)

fig, ax = plt.subplots()

ax.scatter(ir_data["cm"], ir_data["read"], label="Observed Data")

input_values = np.linspace(30,60,300)
ax.plot(input_values, [coeff/x for x in input_values], color="orange",
	label="Fitted Curve")

ax.set_xlabel("Distance (cm)")
ax.set_ylabel("Voltage Output (V)")
ax.set_title("Distance versus Voltage Output for an IR Sensor")

fig.legend(loc="center right")
fig.savefig("ir_calibration.png")

plt.show()