import json
import matplotlib as mlp
import matplotlib.pyplot as plt
import csv
import numpy as np

def get_jsonData():
    data = list()
    with open("bönschDatagrösser.json", "r") as f:
        jsonData = json.load(f)
        for i in jsonData:
            data.append(list(i.keys())[0])
    return data


def get_csv_data():
    data = list()
    with open(r"file5.csv", "r") as f:
         jsonData = csv.reader(f, delimiter=";")
         for i in jsonData:
             data.append(i[0])
    return data

data = get_csv_data()

how_many_games = len(data)
#data = get_jsonData()
x_list = list()
y_list = list()
for i in range(1, 102):
    x_list.append(i)
    y_list.append(data.count(str(i)))

print(len(data))
print(data.count("1000001"))
print(x_list)
print(y_list)
for counter, i in enumerate(y_list):
    wahescheinlichkeit = i/how_many_games
    print(f"{counter}: {wahescheinlichkeit}")
plt.ylabel('Quadratzahlen')

#x_list.pop()
# Einen x-y-Plot erstellen:
plt.plot(x_list, y_list, linestyle='dashed')

plt.show()