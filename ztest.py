import statistics, csv, random
from numpy.lib.function_base import average
import plotly.figure_factory as ff
import pandas as pd
import plotly.graph_objects as go

df = pd.read_csv("data1.csv")
data = df["Math_score"].tolist()


fig = ff.create_distplot([data], ["Math Score"], show_hist=False)
fig.show()

# finding mean
data_mean = statistics.mean(data)

std_dev = statistics.stdev(data)

print(f"Mean is {data_mean}")
print(f"standard deviation is {std_dev}")
