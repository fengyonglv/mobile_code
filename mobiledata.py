from sklearn import preprocessing
from sklearn.decomposition import PCA
from sklearn.preprocessing import MinMaxScaler
import numpy as np
import os
import random
from sklearn.externals import joblib

np.set_printoptions(threshold='nan')

def loadDataSet(fileName):
    numFeat = len(open(fileName).readline().split('\t')[0].split(','))
    # print numFeat
    dataMat = []
    fr = open(fileName)
    for line in fr.readlines():
        lineArr = []
        curline = line.strip().split('\t')[0].split(',')
        for i in range(3,numFeat):
            lineArr.append(curline[i])
        dataMat.append(lineArr)
    return dataMat

dir = 'D:\mobiledata\datanev'
# impute = preprocessing.Imputer(strategy='most_frequent')
pca_model = joblib.load('pca_9_9639.pkl')
scale_model = joblib.load('Scaler_Model.pkl')
pcascale = joblib.load('pcascale.pkl')
datapca = []
datapca_append = []
pca_ratio = []
for file in os.listdir(dir) :

    filename = os.path.join(dir,file)
    print filename
    dataread = np.loadtxt(filename)
    data_scaler = scale_model.transform(dataread)
    datapca = pca_model.transform(data_scaler)
    datapca_scale = pcascale.transform(datapca)
    # datapca_scaler = MinMaxScaler().fit_transform(datapca)
    if len(set(datapca_scale[0])) == 1 :
        continue
    datapca_append.append(datapca_scale)

print len(datapca_append)
np.save("pcadata",datapca_append)

datapca = []
datapca_append = []
dir_positive = 'D:\mobiledata\datapos'

filename = []
for file in os.listdir(dir_positive) :
    filename.append(os.path.join(dir_positive,file))
file_random = set([])
while len(file_random)< 2000 :
    file_random.add(random.randint(0,len(filename)))

for file in file_random :
    # filename = os.path.join(dir_positive,file)
    print filename[file]
    dataread = np.loadtxt(filename[file])
    data_scaler = scale_model.transform(dataread)
    datapca = pca_model.transform(data_scaler)
    datapca_scale = pcascale.transform(datapca)
    # dataread = impute.fit_transform(dataread)
    # dataread = MinMaxScaler().fit_transform(dataread)
    # datapca=MinMaxScaler().fit_transform(pca.fit_transform(dataread))
    # datapca = pca.fit_transform(dataread)
    # datapca_scaler = MinMaxScaler().fit_transform(datapca)

    if len(set(datapca_scale[0])) == 1 :
        continue
    datapca_append.append(datapca_scale)
print len(datapca_append)
np.save("pcadata_positive",datapca_append)
