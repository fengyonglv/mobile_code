# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd

dir_path = "../data_test/0.txt"

data_read = pd.read_table(dir_path , sep=',' ,header=None)
print data_read.dtypes