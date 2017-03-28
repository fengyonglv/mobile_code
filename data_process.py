
# -*- coding: utf-8 -*-

import numpy as np
import os


# import sys

# import paramiko
# client = paramiko.SSHClient()
# client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# client.connect('192.168.88.250', 22, username='frnt', password='frnt', timeout=4)
# #stdin, stdout, stderr  = client.exec_command('cd /proc;cat meminfo')
# stdin, stdout, stderr  = client.exec_command('ls')
# print stdout.read()
# client.close()

def loadDataSet(fileName):
    numFeat = len(open(fileName).readline().split('\t')[0].split(','))
    print numFeat
    # print numFeat
    dataMat = []
    fr = open(fileName)
    for line in fr.readlines():
        lineArr = []
        curline = line.strip().split('\t')[0].split(',')
        print len(curline)
        for i in range(numFeat):
            lineArr.append(curline[i])
        dataMat.append(lineArr)
    return dataMat


# qiehuan_id = []
# fr = open('D:/mobiledata/qiehuan_ID.txt')
# for line in fr.readlines():
#     qiehuan_id.append(line)
# print qiehuan_id[1]

# os.system("grep " + " '" + qiehuan_id[1] "")


data = loadDataSet('C:/Users/feng/Desktop/1.txt')
# data = loadDataSet('D:/mobiledata/FENG25.txt')

print len(data[0])
# data = np.array(data[0:50])


# data[data =='null'] = np.nan
# print (data[0])
# print data[0][1].split()[1].split(':') #0 代表小时 1代表分钟

# print len(data25[0])
#
# data = xlrd.open_workbook('D:/mobiledata/xinqiehuanchenggonglv.xlsx')
# sheet = data.sheets()[0]
# rows = sheet.nrows   #行数
# print rows


# print line
# curline = line.strip().split('\t')[0].split(',')
# time = curline[1]
# cellid = curline[2]

# print cellid
# for row in rows:

# print sheet.cell(3,0)
# print sheet.cell(5,0)
# print sheet.cell(2,1)
# time = sheet.cell(1,1)
# print  time
# time = xlrd.xldate_as_tuple(sheet.cell(2,1).value,0)
#
# print time
# mouth_time = str(time[1])
# print mouth_time
# if len(str(time[2])) == 1 :
#     file_name = str(time[1]) + '0'+str(time[2])+'.txt'
# else:
#     file_name = str(time[1]) + str(time[2]) + '.txt'
# print file_name