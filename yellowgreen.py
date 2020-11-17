## Load file##

import csv
import operator
fn = 'green_tripdata.csv'

## print len of data rows ##
f = open(fn, 'r')
n = 0 
for line in f: 
	n+=1
	if n % 100000 ==0:
		print(n)
print(n)

'''
#print sample data from each field
f = open(fn,'r')
reader = csv.reader(f)
#next(reader, None) #skips header
n=0

for row in reader:
    print(row[0:20])
    if n > 5:
        break
    n+=1
'''    
