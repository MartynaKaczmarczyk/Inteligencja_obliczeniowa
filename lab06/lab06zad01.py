import pandas as pd
import numpy as np
from mlxtend.frequent_patterns import apriori, association_rules
import matplotlib.pyplot as plt

df = pd.read_csv("titanic.csv")

# for col in df:
#     items.update(col)
# print(items)

from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori, association_rules

# Konwersja danych do formatu odpowiedniego dla algorytmu Apriori
data = df[['Class', 'Sex', 'Age', 'Survived']].values.tolist()

# Inicjalizacja i dopasowanie transformaty transakcji
te = TransactionEncoder()
te_ary = te.fit(data).transform(data)
df = pd.DataFrame(te_ary, columns=te.columns_)

# Wyświetlenie przekształconych danych
print(df.head())

# Znalezienie częstych zbiorów
frequent_itemsets = apriori(df, min_support=0.005, use_colnames=True)

# Wyświetlenie częstych zbiorów
print(frequent_itemsets.head())

# Znalezienie reguł asocjacyjnych
rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=0.8)

# Posortowanie reguł według ufności
rules = rules.sort_values(by='confidence', ascending=False)

# Wyświetlenie reguł
print(rules.head())

import matplotlib.pyplot as plt

# Wykres wsparcia vs ufności
plt.scatter(rules['support'], rules['confidence'], alpha=0.5)
plt.xlabel('Support')
plt.ylabel('Confidence')
plt.title('Support vs Confidence')
# plt.show()

# Wykres Lift vs Confidence
plt.scatter(rules['lift'], rules['confidence'], alpha=0.5, color='r')
plt.xlabel('Lift')
plt.ylabel('Confidence')
plt.title('Lift vs Confidence')
# plt.show()


interesting_rules = rules[(rules['confidence'] > 0.8) & (rules['lift'] > 1)]
print(interesting_rules[['antecedents', 'consequents', 'support', 'confidence']])



# itemset = set(items)
# encoded_vals = []
# for index, row in df.iterrows():
#     rowset = set(row)
#     labels = {}
#     uncommons = list(itemset - rowset)
#     commons = list(itemset.intersection(rowset))
#     for uc in uncommons:
#         labels[uc] = 0
#     for com in commons:
#         labels[com] = 1
#     encoded_vals.append(labels)
# encoded_vals[0]ohe_df = pd.DataFrame(encoded_vals)