# -*- coding: utf-8 -*-

from sklearn import preprocessing
from sklearn.decomposition import PCA
from sklearn.preprocessing import MinMaxScaler
import numpy as np
import os
import random

np.set_printoptions(threshold='nan')

# print filename

def loadDatalist(fileName):
    datalist = []
    fr = open(fileName)
    for line in fr.readlines():
        datalist.append(line)
    fr.close()
    return datalist

dir_path = 'D:\mobiledata\data7\chongfu_quan'

filename_list = []
for file in os.listdir(dir_path):
    filename = os.path.join(dir_path,file)
    filename_list.append(filename)

for filenumber_id in filename_list:

    print filenumber_id
    datalist = loadDatalist(filenumber_id)
    id_name = []
    id_number = []
    for line in datalist:
        id_name.append(line.strip().split('\t')[0].split(',')[2])
        id_number.append(line.strip().split('\t')[0].split(',')[3])

    id_set = set(id_name)
    id_set_list = list(id_set)
    classify = [[] for i in range(len(id_set))]
    line_number = 0
    for id_name_one in id_name :
        classify[id_set_list.index(id_name_one)].append(datalist[line_number])
        line_number +=1

    for file_number in range(len(classify)) :
        if file_number == 0 :
            newfile_name = str(str(filenumber_id).split('.')[0].split('\\')[-1])
        else:
            newfile_name = str(str(filenumber_id).split('.')[0].split('\\')[-1])+'_'+str(file_number)
        write_path = dir_path + '\\'+newfile_name +'.txt'
        file = open(write_path, 'w')
        for i in classify[file_number]:
            file.write(i)
        file.close()