import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.metrics import classification_report

df = pd.read_csv("iris1.csv")

iris_variety_mapping = {
    'Setosa': 0,
    'Versicolor': 1,
    'Virginica': 2
}

# Zmapuj nazwy odmian na cyfry
y = df['variety'].map(iris_variety_mapping)
X = df.drop('variety', axis=1)

# Podział 70/30
X_train, X_test, labels_train, labels_test = train_test_split(X, y, test_size=0.3, random_state=285767)

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()

# we fit the train data
scaler.fit(X_train)

# scaling the train data
train_data = scaler.transform(X_train)
test_data = scaler.transform(X_test)

#================================== Sieć neuronowa z jedną warstwą i 2 neuronami ================================
clf = MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(2,), random_state=1)
clf.fit(train_data, labels_train)

predictions_test = clf.predict(test_data)
print(accuracy_score(predictions_test, labels_test))
print(confusion_matrix(predictions_test, labels_test))

print(classification_report(predictions_test, labels_test))

#================================== Sieć neuronowa z jedną warstwą z 3 neuronami =================================
clf = MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(3,), random_state=1)
clf.fit(train_data, labels_train)

predictions_test = clf.predict(test_data)
print(accuracy_score(predictions_test, labels_test))
print(confusion_matrix(predictions_test, labels_test))

print(classification_report(predictions_test, labels_test))

#================================== Sieć neuronowa z dwoma warstwami z 3 neuronami na każdej =================================
clf = MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(3, 2), random_state=1)
clf.fit(train_data, labels_train)

predictions_test = clf.predict(test_data)
print(accuracy_score(predictions_test, labels_test))
print(confusion_matrix(predictions_test, labels_test))

print(classification_report(predictions_test, labels_test))