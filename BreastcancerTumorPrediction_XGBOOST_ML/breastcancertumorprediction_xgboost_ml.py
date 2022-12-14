# Importing the basic libraries
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split

"""### Load Dataset from Local Directory"""

from google.colab import files
uploaded = files.upload()

"""### Importing the dataset"""

dataset = pd.read_csv('dataset.csv')
print(dataset.shape)
print(dataset.head(5))

"""### Segragating Dataset"""

X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values

"""###Splitting Dataset into Train & Test"""

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

"""### Training with XGBoost"""

from xgboost import XGBClassifier
classifier = XGBClassifier()
classifier.fit(X_train, y_train)

"""###Forming Confusion Matrix"""

from sklearn.metrics import confusion_matrix, accuracy_score
y_pred = classifier.predict(X_test)
cm = confusion_matrix(y_test, y_pred)
print(cm)
accuracy_score(y_test, y_pred)

"""###K-Fold Cross Validation """

from sklearn.model_selection import cross_val_score
accuracies = cross_val_score(estimator = classifier, X = X_train, y = y_train, cv = 10)
print("Accuracy: {:.2f} %".format(accuracies.mean()*100))
