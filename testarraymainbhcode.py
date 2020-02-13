import readcol
import numpy as np
files = readcol.readcol('/home/shared/data/h148/testarraymainbh.orbit')
A_files = np.array(files)
sorted_files = np.sort(A_files)
print (sorted_files)
