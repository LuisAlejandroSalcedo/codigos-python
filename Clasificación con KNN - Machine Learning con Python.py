import sklearn
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neightbors import KNeighborsClassifier

iris = load_iris()

x_train, x_test, y_train, y_test = train_test_split(iris['data'], iris['target'])

knn = KNeighborsClassifier(n_neighbors=13)
knn.fit(x_train, y_train)
print(knn.predict([[1.4,5.4,2.3,1.0]]))
