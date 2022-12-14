#Import Libraries*
"""

import pandas as pd
from sklearn.linear_model import LinearRegression

"""### *Load Dataset from Local Directory*"""

from google.colab import files
uploaded = files.upload()

"""### *Load Dataset*"""

dataset = pd.read_csv('data.csv')

"""### *Load Summarize*"""

print(dataset.shape)
print(dataset.head(5))

"""### *Finding & Removing NA values from our Features X*"""

dataset.columns[dataset.isna().any()]

dataset.hours = dataset.hours.fillna(dataset.hours.mean())

"""### *Segregate Dataset into Input X & Output Y*"""

X = dataset.iloc[:, :-1].values
print(X.shape)
X

Y = dataset.iloc[:, -1].values
Y

"""### *Training Dataset using Linear Regression*"""

model = LinearRegression()
model.fit(X,Y)

"""### *Predicted Price for Land sq.Feet of custom values*"""

a=[[9.2,20,0]]
PredictedmodelResult = model.predict(a)
print(PredictedmodelResult)
