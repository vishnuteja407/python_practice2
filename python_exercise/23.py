# import requests

# res = requests.get("https://pythonhow.com/media/data/sampledata.txt")
# data = []

# for txt in res.text.split("\n"):
#     if txt.split(",")[0].isalpha():
#         data.append(txt)
#     else:
#         i , j = txt.split(",")
#         result = f"{int(i)**2},{int(j)**2}"
#         data.append(str(result))

# print(data)
# with open("sampledata_x_2.txt", "w+") as f_data:
#         f_data.write("\n".join(data))


import pandas
     
data = pandas.read_csv("https://pythonhow.com/media/data/sampledata.txt")
data_2 = data * 2
data_2.to_csv("sampledata_x_2.txt", index=None)