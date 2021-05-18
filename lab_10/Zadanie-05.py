# Zadanie 5
# Korzystając ze zbioru danych Iris (https://archive.ics.uci.edu/ml/datasets/iris) wygeneruj wykres punktowy, gdzie wektor x to wartość ‘sepal
# length’ a y to ‘sepal width’, dodaj paletę kolorów c na przykładzie listingu 6 a parametr s niech będzie wartością absolutną z różnicy wartości
# poszczególnych elementów wektorów x oraz y.


import matplotlib.pyplot as plt
from sklearn import datasets

iris = datasets.load_iris()

plt.scatter(iris.data[:, 0], iris.data[:, 1], c=iris.target,s=abs(iris.data[:, 0]-iris.data[:, 1]))

plt.xlabel("sepal length")
plt.ylabel("sepal width")
plt.show()
