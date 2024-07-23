import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.naive_bayes import GaussianNB

df = pd.read_csv("../lab04/iris1.csv")

# Split into training and testing sets
X = df.drop('variety', axis=1)
y = df['variety']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state= 285767)

# Standardize features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

#==============11-NN===========================
# Train KNeighborsClassifier without feature names
classifier11 = KNeighborsClassifier(n_neighbors=11)
classifier11.fit(X_train_scaled, y_train)

# Make predictions
y_pred11 = classifier11.predict(X_test_scaled)

# Evaluate accuracy
acc11 = classifier11.score(X_test_scaled, y_test)
print("Accuracy dla 11-NN wynosi:", round(acc11, 4)*100, "%")

conf_matrix11 = confusion_matrix(y_test, y_pred11)
print("Macierz błędów:")
print(conf_matrix11)

#==============KK5===========================
# Train KNeighborsClassifier without feature names
classifier5 = KNeighborsClassifier(n_neighbors=5)
classifier5.fit(X_train_scaled, y_train)

# Make predictions
y_pred5 = classifier5.predict(X_test_scaled)

# Evaluate accuracy
acc5 = classifier5.score(X_test_scaled, y_test)
print("Accuracy dla 5-NN wynosi:", round(acc5, 4)*100, "%")
conf_matrix5 = confusion_matrix(y_test, y_pred5)
print("Macierz błędów:")
print(conf_matrix5)

#==============KK3===========================
# Train KNeighborsClassifier without feature names
classifier3 = KNeighborsClassifier(n_neighbors=3)
classifier3.fit(X_train_scaled, y_train)

# Make predictions
y_pred3 = classifier3.predict(X_test_scaled)

# Evaluate accuracy
acc3 = classifier3.score(X_test_scaled, y_test)
print("Accuracy dla 3-NN wynosi:", round(acc3, 4)*100, "%")
conf_matrix3 = confusion_matrix(y_test, y_pred3)
print("Macierz błędów:")
print(conf_matrix3)

#=====================NAIVE BAYES=======================

naive_bayes = GaussianNB()
naive_bayes.fit(X_train_scaled, y_train)
nb_predictions = naive_bayes.predict(X_test_scaled)

nb_accuracy = accuracy_score(y_test, nb_predictions)
nb_conf_matrix = confusion_matrix(y_test, nb_predictions)

print("Naive Bayes:")
print("Accuracy dla NB wynosi:", round(nb_accuracy, 2)*100, "%")
print("Macierz błędów:")
print(nb_conf_matrix)

# Virginica jest mylona z Versiclorem i odwrotnie
#Poza tym najlepsze accuracy miały: 5-NN, NB