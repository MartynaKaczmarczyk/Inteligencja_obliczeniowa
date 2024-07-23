import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

df = pd.read_csv("iris1.csv", names=['sepal length','sepal width','petal length','petal width','variety'], skiprows=[0])

#ODZIELENIE DANYCH
features = ['sepal length', 'sepal width', 'petal length', 'petal width']
x = df.loc[:, features].values
y = df.loc[:,['variety']].values


#OBLICZANIE ZE WZORU STRATY INFORMACJI
pca = PCA(n_components=4)
pca.fit(x)
explained_variance_ratio = pca.explained_variance_ratio_
cumulative_variance_ratio = explained_variance_ratio.cumsum()
components_to_keep = (cumulative_variance_ratio >= 0.95).argmax() + 1
print("Starty infromacji dla przypadków: ", cumulative_variance_ratio)
print("Liczba składowych głównych do zachowania:", components_to_keep)
#Wynik: [0.92461872 0.97768521 0.99478782 1]. Program policzył stratę informacji dla liczby kolumn i z danych wynika, że należy zachować dwie główne składowe, by strata informacji była poniżej 5%. W tym przypadku starta wynosi około 2%. W przypadku usunięcia jedenj kolumny starta jest minimalna.

# STANDARYZACJA
x = StandardScaler().fit_transform(x)
pca = PCA(n_components=2)
principalComponents = pca.fit_transform(x)
principalDf = pd.DataFrame(data = principalComponents
             , columns = ['principal component 1', 'principal component 2'])

#POŁĄCZENIE Z GATUNKIEM
finalDf = pd.concat([principalDf, df[['variety']]], axis = 1)
print(finalDf)

#WYKRES 2D
fig = plt.figure(figsize = (8,8))
ax = fig.add_subplot(1,1,1)
ax.set_xlabel('Principal Component 1', fontsize = 15)
ax.set_ylabel('Principal Component 2', fontsize = 15)
ax.set_title('2 component PCA', fontsize = 20)

targets = ["Setosa", "Versicolor", "Virginica"]
colors = ['r', 'g', 'b']
for target, color in zip(targets, colors):
    indicesToKeep = finalDf['variety'] == target
    ax.scatter(finalDf.loc[indicesToKeep, 'principal component 1']
               , finalDf.loc[indicesToKeep, 'principal component 2']
               , c = color
               , s = 50)
ax.legend(targets)
ax.grid()
plt.show()


