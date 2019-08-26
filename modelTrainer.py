
#!/usr/bin/python3
# enable debugging
import cgitb
cgitb.enable()

from keras.models import Sequential
from keras.layers import Dense
import numpy
from numpy import array
# fix random seed for reproducibility
numpy.random.seed(7)
dataset = numpy.loadtxt("malwareHashes.csv")

# split into input (X) and output (Y) variables
X = dataset[:,0:1]
Y = dataset[:,1]

model = Sequential()
model.add(Dense(12, input_dim=1, activation='relu'))
model.add(Dense(8, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
model.fit(X, Y, epochs=300, batch_size=15, verbose=0)

scores = model.evaluate(X, Y)

import sys
def main(gsr):
        print(model.predict(array([gsr]))[0][0])
if __name__ == '__main__':
        main(float(sys.argv[1]))