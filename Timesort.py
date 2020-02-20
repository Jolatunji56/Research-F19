import readcol
import numpy as np
file= readcol.readcol('/home/shared/data/h148/mainbh.orbit')

Time_conversion= 1 
time= file[:,1] * Time_conversion
time_sort= np.argsort(time)
# sorts the time column in data file

