import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.metrics import classification_report

df = pd.read_csv("diabetes.csv")
variety_mapping = {
    'tested_positive': 0,
    'tested_negative': 1,
}
y = df['class'].map(variety_mapping)
X = df.drop('class', axis=1)

# Podział 70/30
X_train, X_test, labels_train, labels_test = train_test_split(X, y, test_size=0.3, random_state=285767)
print(X_train)
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()


# we fit the train data
scaler.fit(X_train)

# scaling the train data
train_data = scaler.transform(X_train)
test_data = scaler.transform(X_test)

clf = MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(6,3), random_state=1, max_iter=500)
clf.fit(train_data, labels_train)

predictions_test = clf.predict(test_data)
print(accuracy_score(predictions_test, labels_test))
print(confusion_matrix(predictions_test, labels_test))

print(classification_report(predictions_test, labels_test))

#Tutaj więcej błędów jest FP (fałszywie pozytywnych) - aż 40. W stosunku do tego błędów fałszywie negatywnych (FN) jest 25.
#W wypadku diagnozy cukrzycy lepiej jest fałszywie wykryć chorobę i zlecić dalsze testy niż ją zignorować, więc lepsze są błędy FP.


clf = MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(3,1), random_state=1, max_iter=500)
clf.fit(train_data, labels_train)

predictions_test = clf.predict(test_data)
print(accuracy_score(predictions_test, labels_test))
print(confusion_matrix(predictions_test, labels_test))

print(classification_report(predictions_test, labels_test))

#Tutaj błędy fałszywej diagnozy choroby się zminiejszyły do 23, lecz błedy nie zauważenia choroby zostały takie same - 25.


