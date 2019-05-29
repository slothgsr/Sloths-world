from pandas import DataFrame, read_csv
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

file = ('bowling.xls')
df = pd.read_excel(file)

t = (df['Unnamed: 1'])

bowlers =[]
scores = []
# print list of bowlers in order
def bowlerlist():
    for i in t.dropna():
        if "Hdcp" not in i:
            if "Team  Team" not in i:
                if "Player" not in i:
                    bowlers.append([i])

def scorelist():
    for i in (df['Unnamed: 74']):
        if i > 10:
            scores.append([int(i)])

bowlerlist()
scorelist()

# print(bowlers)
# print(scores)

x = 0
for i in bowlers:
    print(i + scores[x])
    x += 1


# prints all totals in order.
# for i in (df['Unnamed: 74']):
#         if i > 10:
#             print(i)