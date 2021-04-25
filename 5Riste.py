import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

Data = pd.DataFrame()
f = open('Input.csv','r')
Data = pd.read_csv(f)
print("Size = ", Data.size)
print("First 10 raws is :", "\n", Data[:10])
print("Random 10 raws is:", "\n", Data.sample(n=10))
print("NaN values in raws", "\n", Data.isna().sum())
Names = Data['ID'].unique().tolist()
print("Number of unique Names", "\n", len(Names))
Mans = 0
for i in Data["SEX"]:
    if i == 1:
        Mans += 1
print("Mans procent is", Mans/len(Data)*100,"%")
print("Womens procent is", (1 - Mans/len(Data)) * 100, "%")

fig = plt.figure()
plt.hist(Data["AGE"])
plt.title('Hist of age')
plt.xlabel("Age")
plt.ylabel("Numbers of people")
plt.grid(True)

defaults = Data["default.payment.next.month"].sum()
No_defaults = len(Data) - defaults
print(defaults)
print(No_defaults)


fig = plt.figure()
plt.bar(["Defaulst","Nodefaults"], [defaults,No_defaults])
plt.title('Hist of defaults')
plt.xlabel("Status")
plt.ylabel("Numbers of people")
plt.grid(True)

plt.show()
#plt.bat()
