import pandas

df_append = pandas.DataFrame()
     
data1 = pandas.read_csv("https://pythonhow.com/media/data/sampledata.txt")
data2 = pandas.read_csv("https://pythonhow.com/media/data/sampledata_x_2.txt")

data3 = pandas.concat([data1, data2])
data3.to_csv("sampledata_x_3.txt", index=None)



import io
import pandas
import requests
     
r = requests.get("https://pythonhow.com/media/data/sampledata.txt")
c = r.content
data1 = pandas.read_csv(io.StringIO(c.decode('utf-8')))
data2 = pandas.read_csv("https://pythonhow.com/media/data/sampledata_x_2.txt")
data12 = pandas.concat([data1, data2])
data12.to_csv("sampledata12.txt", index=None)