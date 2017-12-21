__author__ = "Luis Salcedo"

import sklearn
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC

#Set de datos
digits = load_digits()
x_train, x_test, y_train, y_test = train_test_split(digits.data, digits.target)

#Entrenamiento
clf = SVC(gamma=0.001, C=100)
clf.fit(x_train, y_train)

#Predicción
clf.predict(digits.data[-1:])
