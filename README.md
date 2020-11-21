# Final Project - Stephanie Trinka - IA626 
-------------------------------------------------
## Introduction - Yellow & Green NYC Taxi Data - April 2019

This repository will examine New York City yellow and green taxi data collected between the period of April 1, 2019 and April 30, 2019 from the taxi and limousine commission (TLC). 
Below are images of the taxi zones covered between the two files. In the assessment to follow, I strive to identify any differences between the yellow and green taxi services. 

![Image of graph](https://github.com/johnsosc/626finalproj/blob/main/Images/map.png)
------------------------------------------------------------------
## Questions

* How do the yellow and green taxi morning/evening commutes compare by distance? by demand?
* Do certain zones overlap? Do the zones not overlap? If not, why?
* Which zones are highest in demand? least?
------------------------------------------------------------------
## Approach
* I will examine the weekday work commute to see any trends between the two services. 
* Weekend data will be omitted.
* Any erroneous or invalid dates outside the month of April 2019 will be removed. 
* My analysis will focus on the morning commute hours (7-10 am) and evening commute hours (4-7pm)
------------------------------------------------------------------------------------------------
## ETL Process

In the original files, there were rows that fell outisde of April 2019 date range. Additionally, my focus for this analysis was only on weekday data, anything outside of these date criteria were removed. 

![Image of graph](https://github.com/johnsosc/626finalproj/blob/main/Images/weekdayfiltering.PNG)
--------------------------------------------------
## Filtering 

I filtered my remaining weekday dataset to show data by the hour. 
![Image of graph](https://github.com/johnsosc/626finalproj/blob/main/Images/FilteringSample.PNG)

--------------------------------------------------------
## Average Trip Distance per Hour - Morning Commute: 7-10AM

I examined the average distance traveled for both yellow and green taxis on weekdays between the hours of 7:00am -10:00am. Below are the results. 

Hour | Green Taxi | Yellow Taxi  |
-------------|-------------|--------|
07 | 101.27 | 163.68 |
08 | 102.32 | 165.63 |
09 | 105.36 | 165.38 |
10 | 106.76 | 165.54 |
**Avg**|**103.93** |**165.06** |
-----------------------------------------------------
## Average Trip Distance per Hour - Evening Commute: 4-7PM

I examined the average distance traveled for both yellow and green taxis on weekdays between the hours of 4:00pm -6:00pm. Below are the results. 

Hour | Green Taxi | Yellow Taxi |
-------------|-------------|--------|
16 |109.71 | 166.09 |
17 |107.02 | 165.36 |
18 |106.15 | 165.62 |
19 |105.97 | 163.37 |
**Avg**|**107.22** | **165.11** |
-------------------------------------
## Green Taxi - Most Active Pick Up & Drop Off Locations - Morning & Evening Commutes ##
In the graphs below, I display the pick up locations with the highest counts of pick up activity for the morning commute and the drop off locations with the highest activity for the evening commute. What is most apparent is that a lot of the pick up locations shown in the morning, re-appear in the evening. This makes sense because this could mean that commuters are returning to their initial pick up locations.

![Image of graph](https://github.com/johnsosc/626finalproj/blob/main/Images/GreenTaxi_PUMorningCount.PNG)
![Image of graph](https://github.com/johnsosc/626finalproj/blob/main/Images/GreenTaxi_DOEveningCount.PNG)
-------------------------------------
## Yellow Taxi - Most Active Pick Up & Drop Off Locations - Morning & Evening Commutes ##

![Image of graph](https://github.com/johnsosc/626finalproj/blob/main/Images/YellowTaxi_PUMorningCount.PNG)
![Image of graph](https://github.com/johnsosc/626finalproj/blob/main/Images/YellowTaxi_DOEveningCount.PNG)