import numpy as np
import csv
files = ('/home/shared/data/h148/mainbh.orbit', 'r')
csv1 = csv.reader(files, delimiter=',')
data = np.loadtxt('/home/shared/data/h148/mainbh.orbit', delimiter=',')
files_array = np.array(files)
f.size
