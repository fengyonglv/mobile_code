# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
import time
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)

dir_path = "../data_test/0.txt"

data_read = pd.read_table(dir_path , sep=',' ,header=None)
# print data_read.dtypes
# for i in range(data_read.shape[1]):
#     print i
#     data_read.icol[]
# data_read = data_read.iloc[:10]
# print data_read == 'null'
# print data_read.iloc[0]=='null'
# print data_read.str.contains('null')
# print data_read == 'null'

global_start_time = time.time()
for cow in range(data_read.shape[1]):
    print cow
    data_copy = data_read.iloc[:,cow]
    if data_copy[[cow]].dtype == object :
        data_copy[data_copy=='null'] = np.nan
        data_read.iloc[:,cow] = data_copy
    if cow>=4 :
        data_read[[cow]] = data_read[[cow]].astype('float')
print data_read.dtypes
print time.time() - global_start_time


# for com in range(data_read.shape[1]):
#     for row in range(data_read.shape[0]):
#         if data_read.iloc[row,com] == 'null':
#             data_read.iloc[row, com] = np.nan
#     if com>=4 :
#         data_read[[com]] = data_read[[com]].astype('float')
# print data_read.dtypes