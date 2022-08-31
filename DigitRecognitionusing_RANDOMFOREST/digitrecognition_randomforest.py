#Importing Basic Library*
"""

import pandas as pd
import numpy as np

"""### *Access Google Drive contents*"""

from google.colab import drive
drive.mount('/content/gdrive')

"""### *Load Dataset*"""

fileName = "Dataset/digit.csv"
dataset = pd.read_csv(fileName)

"""### *Summarize Dataset*"""

print(dataset.shape)
print(dataset.head(5))

"""### *Segregate Dataset into X(Input/IndependentVariable) & Y(Output/DependentVariable)*"""

X = dataset.iloc[:,1:]
print(X)
print(X.shape)

Y = dataset.iloc[:,0]
print(Y)
print(Y.shape)

"""### *Splitting Dataset into Test & Train*"""

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size = 0.25, random_state = 0)

"""### *Training*"""

from sklearn.ensemble import RandomForestClassifier
model = RandomForestClassifier()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

"""### *Model Accuracy*"""

from sklearn.metrics import accuracy_score
print("Accuracy of the Model: {0}%".format(accuracy_score(y_test, y_pred)*100))

import matplotlib.pyplot as plt
index=10
print("Predicted " + str(model.predict(X_test)[index]))
plt.axis('off')
plt.imshow(X_test.iloc[index].values.reshape((28,28)),cmap='gray')
