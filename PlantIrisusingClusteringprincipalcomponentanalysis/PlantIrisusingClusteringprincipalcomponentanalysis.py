#Importing the basic libraries
"""

from sklearn import datasets
import matplotlib.pyplot as plt

"""## Importing the dataset"""

dataset = datasets.load_iris()

"""### Dataset Segregation"""

X = dataset.data
y = dataset.target
names = dataset.target_names

"""### Fitting the PCA clustering to the dataset with n=2"""

from sklearn.decomposition import PCA
model = PCA(n_components=2) #Number of components to keep
y_means = model.fit(X).transform(X)

"""### Variance Percentage"""

plt.figure()
colors = ['red', 'green', 'orange']

for color, i, target_name in zip(colors, [0, 1, 2], names):
    plt.scatter(y_means[y == i, 0], y_means[y == i, 1], color=color, lw = 2, label=target_name)
plt.title('IRIS Clusterring')
plt.show()
