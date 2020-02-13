import numpy as np
import csv
import operator
import readcol
files = readcol.readcol('/home/shared/data/h148/testarraymainbh.orbit')
csv1 = csv.reader(files, delimiter=',')
sort = np.sorted(csv1, key=operator.itemgetter(0))
for eachline in sort:
	print (eachline)
print files.ndim
print files [0:, 1]
