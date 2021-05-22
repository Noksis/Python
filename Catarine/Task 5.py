Подключили библиотеки
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

Функия для чтения из файла(название вводится) в файл
На вывод.
def input(name):
    F = open(name,'r')
    DEFAULTS = pd.read_csv(F)
    return DEFAULTS

На переменную DEFAULTS записываем вначале пустую структуру,
Потом выодим в структуру через функцию
DEFAULTS = pd.DataFrame()
DEFAULTS = input('input.csv')

# 1
Выводим ответы на 1 вопрос
print(len(DEFAULTS))
print(DEFAULTS[:10])
print(DEFAULTS.sample(n=10))

# 2 
Выводим маску ответов на второй
print(DEFAULTS.isna().sum())
# 3 
Узнаем длину ID
print(len(DEFAULTS.ID))


# 4
Посчитать кол-во мужчин и жегщин в процентах
SEX = DEFAULTS['SEX'].value_counts(normalize=True) * 100 
print("Womens:", SEX[2], "%")
print("Mans:", SEX[1], "%")

# 5
Используем новую графическую библиотеку
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
Используем библиотеку для вывода графика
fig = plt.figure()
plt.bar(["default", "no default"], [Df/len(DEFAULTS)*100,NoDf/len(DEFAULTS)*100])
plt.title('Defaults')
plt.xlabel("Defaults")
plt.ylabel("Procent (%)")
plt.grid(True)

plt.show()
