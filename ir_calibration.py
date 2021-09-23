import pandas as pd
from scipy.optimize import curve_fit

ir_data = pd.read_csv("ir_calibration.csv")

print(curve_fit(lambda x, a: a/x,ir_data["cm"], ir_data["read"])[0][0])