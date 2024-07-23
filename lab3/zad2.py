import pandas as pd
from sklearn.tree import export_text
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import confusion_matrix

df = pd.read_csv("../lab04/iris1.csv")

# Podział na cechy i etykiety
X = df.drop('variety', axis=1)
y = df['variety']

# Podział 30/70
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=285767)

print("Rozmiar zbioru treningowego:", X_train.shape)
print("Rozmiar zbioru testowego:", X_test.shape)

clf = DecisionTreeClassifier(random_state=42)

# Trening
clf.fit(X_train, y_train)

# Wyświetlenie drzewa
tree_text = export_text(clf, feature_names=X.columns.tolist())
print(tree_text)

y_pred = clf.predict(X_test)
accuracy = clf.score(X_test, y_test)
print("Dokładność klasyfikatora:", round(accuracy, 2)*100, "%")

# Macierzy błędów
conf_matrix = confusion_matrix(y_test, y_pred)
print("Macierz błędów:")
print(conf_matrix)
