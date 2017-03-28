
import numpy as np
from sklearn import preprocessing
from sklearn.decomposition import PCA
from sklearn.preprocessing import MinMaxScaler
import random

np.set_printoptions(threshold='nan')

def datashuffle(path_datanev , path_dataposi) :
    datanev_pca = np.load(path_datanev)
    dataposi_pca = np.load(path_dataposi)
    X_train = datanev_pca
    Y_train = [[0 ,1]]*len(X_train)
    index = [i for i in range(len(X_train))]
    random.shuffle(index)
    X_train = X_train[index]

    nev_lennumber = int(len(X_train)*0.8)

    X_validation = X_train[nev_lennumber:]
    Y_validation = Y_train[nev_lennumber:]

    X_train = X_train[:nev_lennumber]
    Y_train = Y_train[:nev_lennumber]

    nev_validation_number = X_validation.shape[0]
    # print nev_validation_number
    X_train = X_train.tolist()
    X_train.extend(dataposi_pca[:-nev_validation_number])
    Y_train.extend([[1,0]]*dataposi_pca[:-nev_validation_number].shape[0])

    X_validation = X_validation.tolist()
    X_validation.extend(dataposi_pca[-nev_validation_number:])
    Y_validation.extend([[1,0]]*dataposi_pca[-nev_validation_number:].shape[0])

    return (np.array(X_train),np.array(Y_train)) ,\
           (np.array(X_validation),np.array(Y_validation))


def train_array_onedimen(path_datanev , path_dataposi):

    (X_train,Y_train) ,(X_validation,Y_validation) = \
        datashuffle(path_datanev,path_dataposi)
    x_train_a = []
    for a in range(X_train.shape[0]):
        x_train_i = []
        for i in range(X_train.shape[2]):
            x_train_i.extend(X_train[a,:,i].tolist())
        x_train_a.append(x_train_i)

    x_validation_a = []
    for a in range(X_validation.shape[0]):
        x_validation_i = []
        for i in range(X_validation.shape[2]):
            x_validation_i.extend(X_validation[a,:,i].tolist())
        x_validation_a.append(x_validation_i)

    return (np.array(x_train_a),Y_train) ,\
           (np.array(x_validation_a),Y_validation)

(X_train,Y_train) ,(X_validation,Y_validation) = \
    train_array_onedimen('pcadata.npy','pcadata_positive.npy')