import random
import plotly.express as px
import scipy
import plotly.figure_factory as pf
import csv
import pandas as pd
df=pd.read_csv('avgdata.csv')
graph = pf.create_distplot([df["Avg Rating"].tolist()], ["Rating"], show_hist=False)
graph.show()
