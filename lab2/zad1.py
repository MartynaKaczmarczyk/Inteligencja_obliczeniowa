import pandas as pd
import math
from difflib import get_close_matches
import numpy as np

df = pd.read_csv("iris_with_errors.csv")


cnt = 0
inRange = 0
wrongNamesCount = 0
i = 2
print("Statystyki bazy danych z błędami:")
namesOfColumnes = ["sepal.length", "sepal.width", "petal.length", "petal.width", "variety"]

for row in df.values:
    column = 0
    for el in row:
        try:
            if el == "-" or math.isnan(el):
                cnt += 1
                print(i, row, "brak statystyki lub nan")
        except:
            try:
                if float(el) < 0 or float(el) > 15:
                    inRange += 1
                    print(i, row, "za mała liczba lub za duża")
                    print(namesOfColumnes[column])
                    numeric_values = df[namesOfColumnes[column]].dropna().values
                    numeric_values = numeric_values[np.where(numeric_values != '-')]
                    numeric_values = pd.to_numeric(numeric_values, errors='coerce').astype(float)
                    median = np.median(numeric_values)
                    df.at[i - 2, namesOfColumnes[column]] = median
                    print("Wartość", row[column], "została zmieniona na", median)
                    print(df.at[i - 2, namesOfColumnes[column]])


            except ValueError:
                if isinstance(el, str) and el not in ["Setosa", "Versicolor", "Virginica"]:
                    available_options = ["Setosa", "Versicolor", "Virginica"]
                    closest_match = get_close_matches(el, available_options, n=1)
                    print(i, row, " Zła nazwa", end="\n")
                    if closest_match:
                        corrected_name = closest_match[0]
                        print(i, row, f" Zła nazwa, poprawiono na: {corrected_name}")
                        row[4] = corrected_name
                    else:
                        print(i, row, "          Nieznana nazwa")
                    wrongNamesCount += 1
                    break
        column += 1
    i += 1


print(cnt, inRange, wrongNamesCount)

