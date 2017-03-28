# -*- coding: utf-8 -*-
import numpy as np
import os
import sys

qiehuan_id = []
fr = open('./qiehuan_ID.txt')
for line in fr.readlines():
    qiehuan_id.append(line.strip())

# print len(qiehuan_id)
# for id in range(1,len(qiehuan_id)):
for id in range(int(sys.argv[1]), int(sys.argv[2])):
    file_name = str(id) +'.txt'
    os.system("grep '" + str(qiehuan_id[id]) + "' ????.txt >" + " ./qiehuanid/" + file_name )
    print file_name+' ok'
# print qiehuan_id[1]
# id =1
# file_name = str(id) +'.txt'
# print file_name
# os.system("grep '" + str(qiehuan_id[id]) + "' ./????.txt >" + " ./qiehuanid/" + file_name )
