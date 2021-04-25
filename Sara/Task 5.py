import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
df = pd.DataFrame()
file = open('Input.csv','r')
df = pd.read_csv(file)
Answer = []
# First task (Index: 0,1,2)
Answer.append("Size:")
Answer.append(df.size)
Answer.append("10:")
Answer.append(df[:10])
Answer.append("Random 10:")
Answer.append(df.sample(n=10))
# Second task (Index: 3)
Answer.append("NaNs:")
Answer.append(df.isna().sum())
# 3 task (Index: 4)
Answer.append("IDs:")
Answer.append(len(pd.unique(df.ID)))
# 4 task (Index: 5)
# (2 is Women and 1 is Mens)
SEX = df['SEX'].value_counts(normalize=True) * 100 
Answer.append("2 = women, 1 = mens")
Answer.append(SEX)

# 5 task 
fig = plt.figure()
plt.title('A Horizontal Bar Chart')
plt.xlabel("Age")
plt.ylabel("Amount")
plt.grid(1)
plt.hist(df.AGE)

# 6 task (Index 6,7)
D = df["default.payment.next.month"].sum()
ND = len(df) - D
Answer.append("default")
Answer.append(D)
Answer.append("normal")
Answer.append(ND)
fig = plt.figure()
plt.pie([D,ND],labels = ["default","No default"],autopct='%1.1f%%')
plt.title('Pie of defaults')
plt.grid(True)

for i in Answer:
    print(i)
plt.show()
