
#!/usr/bin/python3
# enable debugging
import cgitb
cgitb.enable()

from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import Adadelta
from keras.utils import to_categorical

from sklearn.model_selection import train_test_split

import math
import pefile
import numpy
from numpy import array
# fix random seed for reproducibility
numpy.random.seed(7)
dataset = numpy.loadtxt("dataset.csv", delimiter=",")
# split into input (X) and output (Y) variables
X = dataset[:,0:54]
Y = to_categorical(dataset[:,54])
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.33)

def normalize(column_id):
    column = []
    for x in range(len(X[0])):
        column.append(X[x][column_id])
    cmax = max(column)
    cmin = min(column)
    for x in range(len(X[0])):
        cval = X[x][column_id]
        if (math.isnan((cval - cmin) / (cmax - cmin))==False):
            X[x][column_id] = (cval - cmin) / (cmax - cmin)
        else:
            X[x][column_id] = 0
    #normalized_data = (data - minimum) / (maximum - minimum)

for x in range(len(X[0])):
    normalize(x)
print("\n\n-----------------")
print(X[0])
print("-----------------\n\n")
model = Sequential()
model.add(Dense(55, input_dim=54, activation='relu'))
model.add(Dense(36, activation='relu'))
model.add(Dense(16, activation='relu'))
model.add(Dense(8, activation='relu'))
model.add(Dense(2, activation='softmax'))

model.compile(loss='binary_crossentropy', optimizer=Adadelta(lr=1.0, rho=0.95, epsilon=None, decay=0.0), metrics=['accuracy'])
model.fit(X_train, Y_train, epochs=10, batch_size=100, shuffle=True)

scores = model.evaluate(X_test, Y_test)
print("\n%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))

weights_json = model.to_json()
with open("model.json", "w") as json_file:
    json_file.write(weights_json)
model.save_weights("model.h5")