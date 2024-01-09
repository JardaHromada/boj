
from sklearn.datasets import load_digits
from sklearn.naive_bayes import GaussianNB
import matplotlib.pyplot as plt
import sklearn.model_selection as skl

data=load_digits()
plt.gray()
plt.matshow(digits.images[85])
plt.show()

print(data.data.shape)

X = data.data
y = data.target
X_train, X_test, y_train, y_test = skl.train_test_split(X, y, test_size=0.50, random_state=42)

umela_inteligence = GaussianNB()
umela_inteligence.fit(X_train, y_train)

umela_inteligence.score(X_test, y_test)

cisla = X_test[124]
cisla

data=load_digits()
plt.gray()
plt.matshow(digits.images[124])
plt.show()

vysledek = umela_inteligence.predict([cisla])[0]
data.target_names[vysledek]

import matplotlib.pyplot as plt
import numpy
from sklearn import metrics

actual = numpy.random.binomial(1,.9,size = 1000)
predicted = numpy.random.binomial(1,.9,size = 1000)

confusion_matrix = metrics.confusion_matrix(actual, predicted)

cm_display = metrics.ConfusionMatrixDisplay(confusion_matrix = confusion_matrix, display_labels = [False, True])

cm_display.plot()
plt.show()
