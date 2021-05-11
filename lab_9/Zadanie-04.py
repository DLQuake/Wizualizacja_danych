# Zadanie 4
# Z repozytorium UCI (http://archive.ics.uci.edu/ml/index.php) pobierz dataset Iris i za pomocą wykresu punktowego (scattered) wyświetl wartość
# 2 wybranych cech tego datasetu. Dla każdego rodzaju kwiatu użyj innego koloru na wykresie. Przykład można znaleźć w galerii wykresów
# biblioteki matplotlib - link w materiałach matplotlib.

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets

iris = datasets.load_iris()

ts = pd.DataFrame(iris.data, columns=iris.feature_names)
plt.scatter(ts["sepal length (cm)"], ts["sepal width (cm)"], c=iris.target)

plt.title("Iris")
plt.xlabel("sepal length (cm)")
plt.ylabel("sepal width (cm)")
plt.show()
