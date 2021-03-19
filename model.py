from keras.models import Sequential
from keras.models import model_from_json
from keras.optimizers import Adadelta

json_file = open('model.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(loaded_model_json)
# load weights into new model
loaded_model.load_weights("model.h5")
print("Loaded model from disk")

# evaluate loaded model on test data
loaded_model.compile(loss='binary_crossentropy', optimizer=Adadelta(lr=1.0, rho=0.95, epsilon=None, decay=0.0), metrics=['accuracy'])

import sys
from math import isnan

def main(args):
        print(loaded_model.predict([[args]], verbose=0))
if __name__ == '__main__':
        i = sys.argv[1:]
        main(list(map(float,i)))