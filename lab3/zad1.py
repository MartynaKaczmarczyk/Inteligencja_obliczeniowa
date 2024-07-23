import pandas as pd
from sklearn.model_selection import train_test_split
import numpy as np

df = pd.read_csv("../lab04/iris1.csv")

#podzial na zbior testowy (30%) i treningowy (70%), ziarno losowosci = 13
(train_set, test_set) = train_test_split(df.values, train_size=0.7,
random_state=285767)

def classify_iris(sl, sw, pl, pw):
    if sl > 4 and sl <= 5.5 and sw >= 2.9 and sw <= 4.4 and pl < 2 and pw <= 0.6:
        return("Setosa")
    elif sl <= 7.7 and sl >= 5.7 and sw >= 2.5 and sw <= 3.4 and pl <= 6.7 and pl >= 4.8 and pw <= 2.5 and pw >= 1.8:
        return("Virginica")
    else:
        return("Versicolor")

good_predictions = 0
len = test_set.shape[0]
for i in range(len):
    print(classify_iris(test_set[i][0], test_set[i][1], test_set[i][2], test_set[i][3]), test_set[i][4], test_set[i][0], test_set[i][1], test_set[i][2], test_set[i][3])
    if classify_iris(test_set[i][0], test_set[i][1], test_set[i][2], test_set[i][3]) == test_set[i][4]:
        good_predictions = good_predictions + 1
print(good_predictions)
print(good_predictions/len*100, "%")


# Indeks kolumny, po której chcesz posortować dane (indeksowane od 0)
column_index = 4

# Indeksy posortowanej tablicy
sorted_indices = np.argsort(train_set[:, column_index])

# Posortowane dane
sorted_train_set = train_set[sorted_indices]

# print(sorted_train_set)