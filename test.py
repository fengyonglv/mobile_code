# -*- coding: utf-8 -*-

from sklearn import preprocessing
from sklearn.decomposition import PCA
from sklearn.preprocessing import MinMaxScaler
import numpy as np
import os

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
    return dataMat , timeMat

dir = 'D:\mobiledata\data4'
fullfile = []
dataprocessnew = []

# def delete_repetition(data):

# for file in os.listdir(dir):
#     filename = os.path.join(dir,file)

data ,time = loadDataSet('D:\mobiledata\data4/1330.txt')
# data = np.array(data)
# newdata = data[:,1:]
# print newdata.shape
print len(time)
# print len(set(data))
new_data = []
sort_time = np.argsort(time, axis=0)
a=0
for line in range(len(data)):
    # print line
    # print sort_time[line]
    if line !=sort_time[line]:
        a = a+1
    new_data.append(data[sort_time[line]])
print a

# print np.array(new_data).shape
# new_data = np.array(new_data)
repetition_data = []
for line in range(len(new_data)-1) :
    if new_data[line] == new_data[line+1] \
            and time[line] == time[line+1]:
        repetition_data.append(line)
print repetition_data
print time
repetition = np.delete(new_data,repetition_data,axis=0)
print repetition.shape

# newdata = np.delete(newdata,repetition_data,axis=1)
# # newdata = newdata.astype(np.float16)
# print newdata.dtype.name
# neww = newdata[0,-5:]
# print neww
# print neww.astype(np.float16)
# print neww.dtype.name
# aa = neww[1]+neww[2]
# print aa
# np.savetxt('newdata.txt',repetition)

#
# a = np.array(a)
# a = np.delete(a,0,axis=1)
# print a

# if a[0].tolist() ==a[1].tolist() :
#     print a

# b = np.delete(a,0,axis=1)
# print b

# for file in os.listdir(dir):
#
#     filename = os.path.join(dir,file)
#     data = loadDataSet(filename)
#     data = np.array(data)
#     # print data
#     data[data =='null'] = np.nan
#     newdata = np.delete(data,0,0)
#     data_rows = newdata.shape[0]
#     onefile = []
#
#     dataprocess = 0
#     count_threshold = 0  #计算阈值小于90连续几次
#     succe_data = np.array(newdata[:,83],dtype=float)
#     print filename
#
#     for i in range(data_rows):
#         if (succe_data[i] <= 90) :
#             count_threshold += 1
#             if count_threshold >= 4 :
#                 if count_threshold == 4 :
#                     if i>=60 :
#                         onefile.append(i)
#                         dataprocess = newdata[i-(4+2+50):i-(4+2),5:]
#                         np.array(dataprocess,dtype=float)
#                         dataprocessnew.append(dataprocess)
#                         # print dataprocess.dtype.name
#
#         else:
#             count_threshold = 0
#
#
#     if len(onefile):
#         fullfile.append(onefile)
#
# # np.save('dataprocess.npy' , dataprocessnew)
# print np.array(fullfile)
# np.savetxt('fullfile' , fullfile)
