import csv
import json

import pandas as pd
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

data_2 = 0

one_to_ten = 0
eleven_to_hundred = 0
range_three = 0
range_four = 0
range_five = 0
range_six = 0
range_seven = 0
with open(r"bönschDatagrösser.json", "r") as f:
    jsonData = json.load(f)
    print(len(jsonData))
with open(r"file.csv", "r") as f:
    data_2 = csv.reader(f, delimiter=";")
    for value in data_2:
        if value[0] == "counter":
            continue
        key = int(value[0])
        # key = int(list(value.keys())[0])
        if key <= 10:
            one_to_ten += 1
        elif key <= 20:
            eleven_to_hundred += 1
        elif key <= 30:
            range_three += 1
        elif key <= 40:
            range_four += 1
        elif key <= 50:
            range_five += 1
        elif 500 < key < 510:
            range_six += 1
        else:
            range_seven += 1

data = [
      ["1 - 10"],
      ["11 - 20"],
      ["21 - 30"],
      ["31 - 40"],
      ["41 - 50"],
      ["500 - 510"],
      ["> 60"]
     ]

my_list =
for i in range(100):



data[0].append(one_to_ten)
data[1].append(eleven_to_hundred)
data[2].append(range_three)
data[3].append(range_four)
data[4].append(range_five)
data[5].append(range_six)
data[6].append(range_seven)

trys = 0
for value in jsonData:
    key = int(list(value.keys())[0])
    trys += key * 4

print(f"trys: {trys}")



df = pd.DataFrame(data,columns=["range","value"])
df.plot(x="range", y=["value"], kind="bar",figsize=(9,8))
print(df)
plt.show()