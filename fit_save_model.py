# -*- coding: utf-8 -*-
from sklearn import preprocessing
from sklearn.decomposition import PCA
from sklearn.preprocessing import MinMaxScaler
import numpy as np
import os
import random
import matplotlib.pyplot as plt
import re
import time
import numpy as np
import datashuffle
from sklearn.feature_selection import VarianceThreshold
from sklearn.externals import joblib

np.set_printoptions(threshold='nan')

def loadDataSet(fileName):
    numFeat = len(open(fileName).readline().split('\t')[0].split(','))
    # print numFeat
    dataMat = []
    timeMat = []
    fr = open(fileName)
    for line in fr.readlines():
        lineArr = []
        curline = line.strip().split('\t')[0].split(',')
        for i in range(3,numFeat):
            if curline[i] == 'null':
                curline[i] = np.nan
            lineArr.append(float(curline[i]))
        dataMat.append(lineArr)
        timeMat.append(curline[1])
    # print fr.names
    fr.close()
    return dataMat , timeMat

def data_deleterepetition(data_origin,time):
    data = []
    sort_time = np.argsort(time,axis=0)
    time.sort()
    for line in range(len(data_origin)) :
        data.append(data_origin[sort_time[line]])
    repetition_index = []
    data = np.array(data)
    for line in range(len(data) - 1):
        if (str(data[line].tolist()) == str(data[line + 1].tolist())) \
                and (time[line] == time[line+1]):
            repetition_index.append(line)
    return np.delete(data,repetition_index,axis=0)

def find_null(newdata):
    isnan_datasum = (np.sum(np.isnan(newdata),axis=1))
    isnan_ratio = isnan_datasum[isnan_datasum>0]/float(newdata.shape[1])
    print np.where(isnan_datasum>0)
    return isnan_ratio

def next_coms_data(newdata,rows,coms):
    if np.isnan(newdata[rows,coms]) :
        return next_coms_data(newdata,rows+1,coms)
    return newdata[rows,coms]

def nan_fill(newdata):
    for rows in range(newdata.shape[0]) :
        for coms in range(newdata.shape[1]):
            if np.isnan(newdata[rows,coms]):
                if rows == 0:
                    newdata[rows, coms] = next_coms_data(newdata,rows+1,coms)
                newdata[rows,coms] = newdata[rows-1,coms]
    # return newdata

dir = 'D:\mobiledata\data7\\chongfu_quan'
# dir = 'D:\mobiledata\data2'
fullfile = []
dataprocessnew = []
start4 = []
var0 = []
pca = PCA(n_components=0.95)
# Scaler_Model = joblib.load( 'Scaler_Model.pkl')
# a=np.array([[1,3],
#             [2,0],
#             [0,1]])
# print Scaler_Model.transform(a)
# joblib.dump(Scaler_Model, 'Scaler_Model.pkl')

newdata_all = []

# pca = joblib.load('filename.pkl')
del_rows = [0L,1L, 69L, 33L, 42L, 51L, 22L, 23L, 24L, 60L]
for file in os.listdir(dir):
    filename = os.path.join(dir,file)
    data,time = loadDataSet(filename)
    # print np.array(data).shape
    data = np.delete(np.array(data),del_rows,axis=1)
    print data.shape
    # print data[0,70]
    newdata = data_deleterepetition(data,time)
    # print find_null(newdata)
    nan_fill(newdata)
    data_rows = newdata.shape[0]
    onefile = []
    start1 = []
    start2 = []
    start3 = []
    dataprocess = 0
    file_number = 1
    count_threshold = 0  #计算阈值小于90连续几次
    succe_data = np.array(newdata[:,70],dtype=float)
    # print newdata[0]
    print newdata.shape
    print filename
    newdata_all.extend(newdata)
    # print pca.explained_variance_ratio_
    # sel = VarianceThreshold()
    # X = sel.fit_transform(newdata)
    # print X.shape
    # newdata_all.extend(newdata_all)

newdata_all = np.array(newdata_all)
print newdata_all.shape
Scaler_Model = MinMaxScaler(feature_range=(0, 1)).fit(newdata_all)
joblib.dump(Scaler_Model, 'Scaler_Model.pkl')
datapca_scaler = Scaler_Model.transform(newdata_all)
# print np.min(datapca_scaler[:,0])
# print datapca_scaler
# print pca.explained_variance_ratio_[0]
pca.fit(datapca_scaler)
print sum(pca.explained_variance_ratio_)
print pca.explained_variance_ratio_
print pca.n_components_
joblib.dump(pca, 'pca_9.pkl')
pcadata = pca.transform(datapca_scaler)
pcascale = MinMaxScaler(feature_range=(0, 1)).fit(pcadata)
joblib.dump(pcascale, 'pcascale.pkl')