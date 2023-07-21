# import pandas as pd
# from matplotlib import pyplot as plt
# # plt.rcParams["figure.figsize"] = [7.00, 7.00]
# # plt.rcParams["figure.autolayout"] = True
# columns = ["x", "y"]
# df = pd.read_csv("https://pythonhow.com/media/data/sampledata.txt", usecols=columns)
# print("Contents in csv file:", df)
# plt.plot(df.x, df.y)
# plt.show()



# import pandas
# import pylab as plt
     
# data = pandas.read_csv("https://pythonhow.com/media/data/sampledata.txt")
# data.plot(x='x', y='y', kind='scatter')
# plt.show()


from bokeh.plotting import figure
from bokeh.io import output_file, show
import pandas
     
output_file("bokeh_plot.html")
data = pandas.read_csv("https://pythonhow.com/media/data/sampledata.txt")
f = figure()
f.triangle(x=data["x"], y=data["y"])
     
show(f)