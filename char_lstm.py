import numpy
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
from keras.utils import np_utils

# define the raw dataset
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# create mapping of characters to integers (0-25) and the reverse
char_to_int = dict((c, i) for i, c in enumerate(alphabet))
int_to_char = dict((i, c) for i, c in enumerate(alphabet))

# prepare the dataset of input to output pairs encoded as integers
seq_length = 3
dataX = []
dataY = []
for i in range(0, len(alphabet) - seq_length, 1):
    seq_in = alphabet[i:i + seq_length]
    seq_out = alphabet[i + seq_length]
    dataX.append([char_to_int[char] for char in seq_in])
    dataY.append(char_to_int[seq_out])
    print seq_in, '->', seq_out

X = numpy.reshape(dataX, (len(dataX), seq_length, 1))
X = X/float(len(dataX))
# print X
# print dataY
y = np_utils.to_categorical(dataY)
print y.shape
# print y
model = Sequential()
model.add(LSTM(32 , input_shape=(X.shape[1], X.shape[2])))
# model.add(Dense(y.shape[1],activation='softmax'))
model.add(Dense(1,activation='linear'))

model.compile(loss='mse',optimizer='adam',metrics =['accuracy'])
model.fit(X,dataY,nb_epoch=200, batch_size=1, verbose=1)
scores = model.evaluate(X, dataY, verbose=0)
print("Model Accuracy: %.2f%%" % (scores[1]*100))
