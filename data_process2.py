
# -*- coding: utf-8 -*-

from sklearn import preprocessing
from sklearn.decomposition import PCA
from sklearn.preprocessing import MinMaxScaler
import numpy as np
import os
import random

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

dir = 'D:\mobiledata\data7\\2000samples'
# dir = 'D:\mobiledata\data7\chongfu_quan'
fullfile = []
dataprocessnew = []
start4 = []
del_rows = [0L,1L, 69L, 33L, 42L, 51L, 22L, 23L, 24L, 60L]

for file in os.listdir(dir):

    filename = os.path.join(dir,file)
    data,time = loadDataSet(filename)
    data = np.delete(np.array(data),del_rows,axis=1)
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
    print filename

    for i in range(data_rows):
        if (succe_data[i] <= 90) :
            count_threshold += 1
            if count_threshold >= 4 :
                if count_threshold == 4 :
                    if i>=60 :
                        onefile.append(i)
                        start1.append(i)
                        # dataprocess = newdata[i-(4+2+50):i-(4+2),2:]
                        # dataprocessnew.append(dataprocess)
                    else:
                        start1.append(i)
        else:
            if count_threshold >=4  :
                # if i >= 61:
                start1.append(i-1)
                start2.append(start1)
                start1 = []
            count_threshold = 0
    if len(start2):
        fullfile.append(onefile)
        if len(start2) >=2 :
            for i in range(len(start2)-1):
                start3.append(start2[i+1][0]-start2[i][1])
            start4.append(start3)

    for i in range(len(start2)):
        if i == 0 :
            if (start2[0][0] >= 60) :
                # print start2[i]
                dataprocess = newdata[start2[i][0] - (4 + 2 + 50):start2[i][0] - (4 + 2)]
                dataprocessnew.append(dataprocess)
                file_path = './datanev/' + str(filename.split('.')[0].split('\\')[-1]) + 'and'+str(file_number)
                np.savetxt(file_path, dataprocess)
                file_number +=1
                # print dataprocess.shape
                # print 'save'
        elif start2[i][0]-start2[i-1][1] >= 60 :
            # print start2[i]
            dataprocess = newdata[start2[i][0] - (4 + 2 + 50):start2[i][0] - (4 + 2)]
            dataprocessnew.append(dataprocess)
            file_path = './datanev/' + str(filename.split('.')[0].split('\\')[-1]) + 'and' +str(file_number)
            np.savetxt(file_path, dataprocess)
            file_number +=1

    if len(start2)<=1:
        file_number = 1
        if len(start2) == 0:
            number = 100
            for i in range(20) :
                dataprocess = newdata[number - (4 + 2 + 50):number - (4 + 2)]
                file_path = './datapos/' + str(filename.split('.')[0].split('\\')[-1]) + 'and' +str(file_number)
                np.savetxt(file_path, dataprocess)
                number +=100
                file_number +=1
                if number >=data_rows:
                    break
        if len(start2) == 1:
            number = 100
            for i in range(20):
                if number < (start2[0][0] -10) :
                    dataprocess = newdata[number - (4 + 2 + 50):number - (4 + 2)]
                    file_path = './datapos/' + str(filename.split('.')[0].split('\\')[-1]) + 'and' + str(file_number)
                    np.savetxt(file_path, dataprocess)
                    number += 100
                    file_number += 1
                    if number >= data_rows:
                        break
                elif number > (start2[0][1] +100) :
                    dataprocess = newdata[number - (4 + 2 + 50):number - (4 + 2)]
                    file_path = './datapos/' + str(filename.split('.')[0].split('\\')[-1]) + 'and' + str(file_number)
                    np.savetxt(file_path, dataprocess)
                    number += 100
                    file_number += 1
                    if number >= data_rows:
                        break

# print np.array(start4)
# print np.array(start2)