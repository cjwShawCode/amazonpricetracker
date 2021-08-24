import pandas as pd
from matplotlib import pyplot as plt

def show(title):
	plt.rcParams["figure.figsize"] = [15.00, 8]
	plt.rcParams["figure.autolayout"] = True
	columns = ["Date", "Price"]
	df = pd.read_csv(f"{title}.csv", usecols=columns)
	plt.plot(df.Date, df.Price)
	plt.title(f"{title} Price History")
	plt.show()