import csv
import operator

files = open ('/home/shared/data/h148/testarraymainbh.orbit', 'r')
csv1 = csv.reader(files,delimiter=',')
sort = sorted(csv1, key=operator.itemgetter(0))

print (sort)
