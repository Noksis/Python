import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def input(name):
    F = open(name,'r')
    DEFAULTS = pd.read_csv(F)
    return DEFAULTS

DEFAULTS = pd.DataFrame()
DEFAULTS = input('input.csv')

# 1
print(len(DEFAULTS))
print(DEFAULTS[:10])
print(DEFAULTS.sample(n=10))

# 2 
print(DEFAULTS.isna().sum())
# 3 
print(len(DEFAULTS.ID))


# 4
SEX = DEFAULTS['SEX'].value_counts(normalize=True) * 100 
print("Womens:", SEX[2], "%")
print("Mans:", SEX[1], "%")

# 5
fig = plt.figure()
plt.title('Hist of Age')
plt.xlabel("Age")
plt.ylabel("Amount")
plt.grid(1)
plt.hist(DEFAULTS.AGE)

# 6 
Df = DEFAULTS["default.payment.next.month"].sum()
NoDf = len(DEFAULTS) - Df
print("Defaults:", Df)
print("No defaults:", NoDf)

fig = plt.figure()
plt.bar(["default", "no default"], [Df/len(DEFAULTS)*100,NoDf/len(DEFAULTS)*100])
plt.title('Defaults')
plt.xlabel("Defaults")
plt.ylabel("Procent (%)")
plt.grid(True)

plt.show()
