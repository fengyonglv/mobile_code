import numpy as np
import datashuffle
from keras.models import Sequential
from keras.layers import Dense,Activation,Dropout
import os
import time
import matplotlib.pyplot as plt
from keras.optimizers import SGD,Adam,RMSprop


(X_train,Y_train) ,(X_validation,Y_validation) = \
    datashuffle.train_array_onedimen('pcadata.npy','pcadata_positive.npy')

model = Sequential()

model.add(Dense(output_dim=300,input_dim=450))
model.add(Dropout(0.5))
model.add(Activation("relu"))
model.add(Dense(200))
model.add(Activation("relu"))
model.add(Dropout(0.3))
model.add(Dense(200))
model.add(Activation("relu"))
model.add(Dropout(0.5))
model.add(Dense(2))
model.add(Activation("softmax"))
# model.load_weights('D:\mobiledata\keras_bp\\0.807631160667_181307\my_model_weights.h5')

sgd = SGD(lr=0.06, momentum=0.2, decay=0.0, nesterov=False)
model.compile(loss='categorical_crossentropy', optimizer='sgd', metrics=['accuracy'])

# hist = model.fit(X_train,Y_train,nb_epoch=100, batch_size=16,validation_data=(X_validation,Y_validation))
hist = model.fit(X_train,Y_train,nb_epoch=80, batch_size=16,validation_split=0.2)
score = model.evaluate(X_validation,Y_validation)
print score
score_plt = [score[1]]*len(hist.history['acc'])
x = [a for a in range(len(hist.history['acc']))]
plt.plot(x , hist.history['acc'],color='red',label='traing acc')
plt.plot(x , hist.history['val_acc'],color='blue',label='val_acc')
plt.plot(x , score_plt,color='g',label='test_acc')
plt.legend(loc='upper left')
path_str = str(max(hist.history.get('val_acc'))) + '_' + \
           str(time.strftime('%H%M%S',time.localtime(time.time())))
os.mkdir('./keras_bp/'+path_str)
save_model_path = './keras_bp/'+path_str+'/my_model_architecture.json'
save_weights_path = './keras_bp/'+path_str+'/my_model_weights.h5'
file_save = open(save_model_path,'w')
file_save.write(model.to_json())
file_save.close()
model.save_weights(save_weights_path)
plt.savefig('./keras_bp/'+path_str+'/acc.jpg')
