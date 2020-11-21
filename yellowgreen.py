## Load file##

import csv
import operator

'''
## print len of data rows ##
f = open(fn, 'r')
n = 0 
for line in f: 
	n+=1
	if n % 100000 ==0:
		print(n)
print(n)
'''
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
'''
# ETL --Remove Weekends and Invalid Dates----###

import pandas as pd
import os
from datetime import datetime
import dateutil.parser

base_dir = os.getcwd()

filename = 'green_tripdata.csv'

filepath = os.path.join(base_dir,filename)

chunk_size = 100000
start_date = '4/1/2019 0:0'
end_date = '4/30/2019 23:59'

start_date = datetime.strptime(start_date,"%m/%d/%Y %H:%M").date()
end_date = datetime.strptime(end_date,"%m/%d/%Y %H:%M").date()


df_parts = pd.read_csv(filepath, chunksize = chunk_size)
output_list = []  # append each chunk df here 


# Each chunk is in df format
for df in df_parts:  
    # perform date filtering 
    #print(df.head())
    df['lpep_pickup_datetime_new'] = df['lpep_pickup_datetime'].apply(lambda x :dateutil.parser.parse(x).date())
    
    #Filtering based on start and end dates
    df = df[(df['lpep_pickup_datetime_new']>=start_date) & (df['lpep_pickup_datetime_new']<=end_date)]

    #Filter based on weekdays
    df['weekdays'] = df['lpep_pickup_datetime_new'].apply(lambda x:x.weekday())
    df = df[df['weekdays']<5]
    df.drop(columns=['weekdays','lpep_pickup_datetime_new'],axis=1,inplace=True)
    
    output_list.append(df)
df = pd.concat(output_list)
save_filename = r'stephanie_green_taxi.csv'

save_filepath = os.path.join(base_dir,save_filename)

df.to_csv(save_filepath)
'''


# Average Distance per Hour
'''
def get_avg(fn):
    f = open(fn,'r')
    reader = csv.reader(f)
    next(reader, None) #skips header

    n=0
    shist={}

    for xx, row in enumerate(reader):
        dts = row[2][1:]
        dtl = dts.split(":")
        hour = dtl[0][10:12]
        k = hour

        try:
            r7 = float(row[6])

            k=hour
            if k in shist.keys():
                shist[k][0] += r7 # row[7] = trip distance
                shist[k][1] += 1 # incrementing counter for that hour
            else:
                shist[k] = [r7, 1] # [trip distance, count]

        except:
            pass

    hr_dict = dict()
    
    for xx, i in enumerate(shist.items()):
        hr = i[0]
        trip_distance = i[1][0]
        count = i[1][1]
#      avg = int(round((trip distance / count)))
        avg = round((trip_distance / count), 2)
    
        hr_dict[hr] = avg
      
    
    return(hr_dict)


fn = 'stephanie_green_taxi.csv'
hour_averages = get_avg(fn)

print()
print("="*40)
print()

total_avg = 0
count2 = 0

for i in hour_averages.items():
    total_avg += i[1]
    count2 += 1
    print(i)

total_avg = (total_avg / count2)

print("total_avg: {:.2f}".format(total_avg))
'''

##Average Distance per PU Location##
'''
def get_avg(fn):
    f = open(fn,'r')
    reader = csv.reader(f)
    next(reader, None) #skips header

    n=0
    shist={}

    for xx, row in enumerate(reader):
        zone = row[8]
        k = zone

        try:
            r7 = float(row[5])

            k=zone
            if k in shist.keys():
                shist[k][0] += r7 # row[7] = num_passengers getting on
                shist[k][1] += 1 # incrementing counter for that zone
            else:
                shist[k] = [r7, 1] # [num_passengers, count]

        except:
            pass

    hr_dict = dict()
    
    for xx, i in enumerate(shist.items()):
        hr = i[0]
        num_passengers = i[1][0]
        count = i[1][1]
#      avg = int(round((num_passengers / count)))
        avg = round((num_passengers / count), 2)
    
        hr_dict[hr] = avg
      
    
    return(hr_dict)


fn = 'stephanie_yellow_taxi.csv'
zone_averages = get_avg(fn)

print()
print("="*40)
print()

total_avg = 0
count2 = 0

for i in zone_averages.items():
    total_avg += i[1]
    count2 += 1
    print(i)

total_avg = (total_avg / count2)

print("total_avg: {:.2f}".format(total_avg))

#Distinct Values (Zones) # 
'''
'''
fn = 'stephanie_green_taxi.csv'

f = open(fn,'r')
reader = csv.reader(f)
next(reader, None) #skips header
   
import operator
shist={}
for row in reader:
        k=row[6] 
        if k in shist.keys():
            shist[k]+=1
        else:
            shist[k]=1
     
print(row[6])

D = dict()
D[6] = []


for row in reader:
    if row[6] not in D[6]:
        D[6].append(row[6])

for i in D.items():
    print(i)
'''    

