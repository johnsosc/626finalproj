# Final Project - Stephanie Trinka - IA626 
-------------------------------------------------
## Introduction - Yellow & Green NYC Taxi Data

This repository contains taxi data collected between the period of April 1, 2019 and April 30, 2019 from the New York City area. In the sections to follow, I examine the fields contained within the file to further investigate what the data is presenting as well as identify and troubleshoot any challenges that exist within the dataset.

-------------------------------------------------
## April 2019 NYC Taxi Data
* Yellow Taxi Data - 7,433,140 rows
* Green Taxi Data - 514,393 rows

--------------------------------------------------
## ETL Process

In the original files, there were rows that fell outisde of April 2019 date range. These were removed. Additionally, my focus for this analysis was only on weekday data, anything outside of this date criteria, were also removed. 

![Image of graph](https://github.com/johnsosc/626finalproj/blob/main/Images/weekdayfiltering.PNG)
--------------------------------------------------
## Average Trip Distance per Hour - Morning Commute
Hour | Green Taxi | Yellow Taxi
-------------|-------------|
07 | 14.12 | 163.68
08 | 13.08 | 165.63
09 | 13.43 | 165.38
10| 13.33  | 165.54
-----------------------------------------------------
## Average Trip Distance per Hour - Evening Commute 
Hour | Green Taxi | Yellow Taxi
-------------|-------------|
16 |13.54 | 166.09
17 |13.57 | 165.36
18 |12.52 | 165.62
19 |11.89 | 163.37

