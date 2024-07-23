import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler, StandardScaler

iris_df = pd.read_csv("iris1.csv", names=['sepal length','sepal width','petal length','petal width','variety'], skiprows=[0])

#WYKRES DLA ORGINALNYCH DANYCH
plt.figure(figsize=(10, 6))
for species in iris_df['variety'].unique():
    plt.scatter(iris_df.loc[iris_df['variety'] == species, 'sepal length'],
                iris_df.loc[iris_df['variety'] == species, 'sepal width'],
                label=species)
plt.xlabel('Sepal Length')
plt.ylabel('Sepal Width')
plt.title('Original Data')
plt.legend()
plt.show()


# ZNORMALIZOWANE DANE MIN-MAX
scaler = MinMaxScaler()
iris_df_mm = iris_df.copy()
iris_df_mm[['sepal length', 'sepal width']] = scaler.fit_transform(iris_df[['sepal length', 'sepal width']])

plt.figure(figsize=(10, 6))
for species in iris_df_mm['variety'].unique():
    plt.scatter(iris_df_mm.loc[iris_df_mm['variety'] == species, 'sepal length'],
                iris_df_mm.loc[iris_df_mm['variety'] == species, 'sepal width'],
                label=species)
plt.xlabel('Sepal Length (Min-Max Scaled)')
plt.ylabel('Sepal Width (Min-Max Scaled)')
plt.title('Min-Max Scaled Data')
plt.legend()
plt.show()


scaler = StandardScaler()
iris_df_z = iris_df.copy()
iris_df_z[['sepal length', 'sepal width']] = scaler.fit_transform(iris_df[['sepal length', 'sepal width']])

# Z-SCORE
plt.figure(figsize=(10, 6))
for species in iris_df_z['variety'].unique():
    plt.scatter(iris_df_z.loc[iris_df_z['variety'] == species, 'sepal length'],
                iris_df_z.loc[iris_df_z['variety'] == species, 'sepal width'],
                label=species)
plt.xlabel('Sepal Length (Z-Score Scaled)')
plt.ylabel('Sepal Width (Z-Score Scaled)')
plt.title('Z-Score Scaled Data')
plt.legend()
plt.show()

# STATYSTYKI
# DANE ORGINALNE
print(iris_df['sepal length'].describe())
print(iris_df['sepal width'].describe())
# count    150.000000
# mean       5.843333
# std        0.828066
# min        4.300000
# 25%        5.100000
# 50%        5.800000
# 75%        6.400000
# max        7.900000
# Name: sepal length, dtype: float64
# count    150.000000
# mean       3.057333
# std        0.435866
# min        2.000000
# 25%        2.800000
# 50%        3.000000
# 75%        3.300000
# max        4.400000
# Name: sepal width, dtype: float64

#Według tego wykresu dla irysów gatunku setosa długość płatków oscyluje wokół wartości 3 - 3.5 cm, a szerokość około 5 cm.
#Dla gatunku versicolor, długość płatków to około 2.5 - 3 cm, a szerkość 6 - 7 cm.
#Dla gatunku virginica długość płatków to około 3 cm, a szerkość to 6.5 - 7.5 cm.
#Dane gatunków versicolor i virginica się na siebie nakładają.

# MIN-MAX
print(iris_df_mm[['sepal length', 'sepal width']].describe())

#        sepal length  sepal width
# count    150.000000   150.000000
# mean       0.428704     0.440556
# std        0.230018     0.181611
# min        0.000000     0.000000
# 25%        0.222222     0.333333
# 50%        0.416667     0.416667
# 75%        0.583333     0.541667
# max        1.000000     1.000000

# Z-SCORE
print(iris_df_z[['sepal length', 'sepal width']].describe())

#        sepal length   sepal width
# count  1.500000e+02  1.500000e+02
# mean  -4.736952e-16 -7.815970e-16
# std    1.003350e+00  1.003350e+00
# min   -1.870024e+00 -2.433947e+00
# 25%   -9.006812e-01 -5.923730e-01
# 50%   -5.250608e-02 -1.319795e-01
# 75%    6.745011e-01  5.586108e-01
# max    2.492019e+00  3.090775e+00

#Chociaż też ostatecznie widać, że virginica jest trochę większą odmianą niż versicolor

#ZAPYTANIE DO CHATU
# Zrób wykresy z irysami jako punktami na wykresie, dla dwóch zmiennych: sepal length i sepal width z legendami o gatunkach irysów: ["Setosa", "Versicolor", "Virginica"] Wykresy mają być w 3 wersjach dane oryginalne, znormalizowane min-max i zeskalowane z-scorem


