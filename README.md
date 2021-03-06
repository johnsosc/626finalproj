# Final Project - Stephanie Trinka - IA626 
---------------------------------------------------------------------------------------
## Introduction - Yellow & Green NYC Taxi Data - April 2019

This repository will examine New York City yellow and green taxi data collected between the period of April 1, 2019 and April 30, 2019 from the taxi and limousine commission (TLC). 
Below are images of the taxi zones covered between the two files. In the assessment to follow, I strive to identify any differences between the yellow and green taxi services. 

![Image of graph](https://github.com/johnsosc/626finalproj/blob/main/Images/map.png)
------------------------------------------------------------------------------------------
## Questions

* How do the yellow and green taxi morning/evening commutes compare by distance? By demand?
* Do certain zones overlap? If not, why?
* Which zones are highest in demand? 
--------------------------------------------------------------------------------------------
## Approach
* I will examine the weekday work commute to see any trends between the two services. 
* Weekend data will be omitted.
* Any erroneous or invalid dates outside the month of April 2019 will be removed. 
* My analysis will focus on the morning commute hours (7-10 am) and evening commute hours (4-7pm)
------------------------------------------------------------------------------------------------
## ETL Process

In the original files, there were rows that fell outisde of April 2019 date range. Additionally, my focus for this analysis was only on weekday data, anything outside of these date criteria were removed. 

![Image of graph](https://github.com/johnsosc/626finalproj/blob/main/Images/DateFilter.PNG)
![Image of graph](https://github.com/johnsosc/626finalproj/blob/main/Images/weekdayfiltering.PNG)
-------------------------------------------------------------------------------------------------
## Filtering 

I filtered my remaining weekday dataset to show data by the hour. 
![Image of graph](https://github.com/johnsosc/626finalproj/blob/main/Images/FilteringSample.PNG)

---------------------------------------------------------------------------------------------------
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

I examined the average distance traveled for both yellow and green taxis on weekdays between the hours of 4:00pm -7:00pm. Below are the results. 

Hour | Green Taxi | Yellow Taxi |
-------------|-------------|--------|
16 |109.71 | 166.09 |
17 |107.02 | 165.36 |
18 |106.15 | 165.62 |
19 |105.97 | 163.37 | 
**Avg**|**107.22** | **165.11** |
-------------------------------------
## Green Taxi - Most Active Pick Up & Drop Off Zone IDs - Morning & Evening Commutes ##
In the graphs below, I display the pick up locations with the highest counts of pick up activity for the morning commute and the drop off locations with the highest activity for the evening commute. What is most apparent is that a lot of the pick up locations shown in the morning, re-appear in the evening. This makes sense because this could mean that commuters are returning to their initial pick up locations.

![Image of graph](https://github.com/johnsosc/626finalproj/blob/main/Images/GreenTaxi_PUMorningCount.PNG)
![Image of graph](https://github.com/johnsosc/626finalproj/blob/main/Images/GreenTaxi_DOEveningCount.PNG)
-------------------------------------
## Yellow Taxi - Most Active Pick Up & Drop Off Zone IDs - Morning & Evening Commutes ##

![Image of graph](https://github.com/johnsosc/626finalproj/blob/main/Images/YellowTaxi_PUMorningCount.PNG)
![Image of graph](https://github.com/johnsosc/626finalproj/blob/main/Images/YellowTaxi_DOEveningCount.PNG)

--------------------------------------------------
## Observations - Trip Distance - Yellow v. Green Taxi
* In both the morning and evening commutes, green taxi had a smaller average distance traveled than the yellow taxi service. 
## Observations - Zone Trip Instances - Yellow v. Green Taxi

### Pick Up Zone ID Analysis
* In both the morning and evening commutes, green taxi had fewer trip instances than the yellow taxi service. 
* The list below represents 75% of the yellow and green of the overall pickup total across the entire survey area
* Below is a descriptive list of the top 30 most active pick up zones for yellow and green taxi during the evening and morning commutes. 

Green Taxi | Yellow Taxi |
-------------|-------------|
74:Manhattan-East Harlem North|237:Manhattan-Upper East Side South
75:Manhattan-East Harlem South|236:Manhattan-Upper East Side North
41:Manhattan-Central Harlem|162:Manhattan-Midtown East
166:Manhattan-Morningside Heights|161:Manhattan-Midtown Center
7:Queens-Astoria|186:Manhattan-Penn Station/Madison Sq West
42:Manhattan-Central Harlem North|170:Manhattan-Murray Hill
82:Queens-Elmhurst|234:Manhattan-Union Sq
33:Brooklyn-Brooklyn Heights|230:Manhattan-Times Sq/Theatre District
95:Queens-Forest Hills|138:Queens-LaGuardia Airport
244:Manhattan-Washington Heights South|142:Manhattan-Lincoln Square East
97:Brooklyn-Fort Greene|48:Manhattan-Clinton East
65:Brooklyn-Downtown Brooklyn/MetroTech|239:Manhattan-Upper West Side South
66:Brooklyn-DUMBO/Vinegar Hill|163:Manhattan-Midtown North
129:Queens-Jackson Heights|141:Manhattan-Lenox Hill West
181:Brooklyn-Park Slope|238:Manhattan-Upper West Side North
130:Queens-Jamaica|140:Manhattan-Lenox Hill East
25:Brooklyn-Boerum Hill|107:Manhattan-Gramercy
260:Queens-Woodside|68:Manhattan-East Chelsea
43:Manhattan-Central Park|164:Manhattan-Midtown South
116:Manhattan-Hamilton Heights|100:Manhattan-Garment District
52:Brooklyn-Cobble Hill|229:Manhattan-Sutton Place/Turtle Bay North
145:Queens-Long Island City/Hunters Point|263:Manhattan-Yorkville West
61:Brooklyn-Crown Heights North|231:Manhattan-TriBeCa/Civic Center
134:Queens-Kew Gardens|90:Manhattan-Flatiron
152:Manhattan-Manhattanville|246:Manhattan-West Chelsea/Hudson Yards
196:Queens-Rego Park|43:Manhattan-Central Park
49:Brooklyn-Clinton Hill|262:Manhattan-Yorkville East
92:Queens-Flushing|113:Manhattan-Greenwich Village North

The map below represents the active pick up zone list above. The plots represent 75% of the overall pickup total across the entire survey area.
It is apparent that the green taxi service range is more comprehensive than the yellow taxi service. 
The Yellow taxi service appears to be a predominantly Manhattan based service (with the exception of LaGuardia Airport), while the green taxi service expands to the other NYC buroughs.
Also, there appears to be little to no overlap among the pick up location zones. 

![Image of graph](https://github.com/johnsosc/626finalproj/blob/main/Images/TopTrips.png)

### Drop Off Zone ID Analysis
* Below is a descriptive list of the top 30 most active drop off zones for yellow and green taxi during the evening and morning commutes.
* This list represents more than 50% of the overall yellow and green drop off zone total across the entire survey area. 
* The first 11 rows are bolded due to an overlap in drop off zone IDs between the yellow and green services

Green Taxi Zone ID | Yellow Zone ID | 
-------------|-------------|
**238:Manhattan-Upper West Side North**|**238:Manhattan-Upper West Side North**
**236:Manhattan-Upper East Side North**|**236:Manhattan-Upper East Side North**
**239:Manhattan-Upper West Side South**|**239:Manhattan-Upper West Side South**
**263:Manhattan-Yorkville West**|**263:Manhattan-Yorkville West**
**237:Manhattan-Upper East Side South**|**237:Manhattan-Upper East Side South**
**142:Manhattan-Lincoln Square East**|**142:Manhattan-Lincoln Square East**
**140:Manhattan-Lenox Hill East**|**140:Manhattan-Lenox Hill East**
**141:Manhattan-Lenox Hill West**|**141:Manhattan-Lenox Hill West**
**162:Manhattan-Midtown East**|**162:Manhattan-Midtown East**
**161:Manhattan-Midtown Center**|**161:Manhattan-Midtown Center**
**231:Manhattan-TriBeCa/Civic Center**|**231:Manhattan-TriBeCa/Civic Center**
74:Manhattan-East Harlem North|163:Manhattan-Midtown North
42:Manhattan-Central Harlem North|100:Manhattan-Garment District
41:Manhattan-Central Harlem|233:Manhattan-UN/Turtle Bay South
75:Manhattan-East Harlem South|143:Manhattan-Lincoln Square West
181:Brooklyn-Park Slope|230:Manhattan-Times Sq/Theatre District
244:Manhattan-Washington Heights South|170:Manhattan-Murray Hill
116:Manhattan-Hamilton Heights|234:Manhattan-Union Sq
82:Queens-Elmhurst|186:Manhattan-Penn Station/Madison Sq West
61:Brooklyn-Crown Heights North|48:Manhattan-Clinton East
25:Brooklyn-Boerum Hill|246:Manhattan-West Chelsea/Hudson Yards
166:Manhattan-Morningside Heights|164:Manhattan-Midtown South
7:Queens-Astoria|68:Manhattan-East Chelsea
129:Queens-Jackson Heights|107:Manhattan-Gramercy
95:Queens-Forest Hills|229:Manhattan-Sutton Place/Turtle Bay North
138:Queens-LaGuardia Airport|79:Manhattan-East Village
97:Brooklyn-Fort Greene|43:Manhattan-Central Park
33:Brooklyn-Brooklyn Heights|113:Manhattan-Greenwich Village North
152:Manhattan-Manhattanville|90:Manhattan-Flatiron
----------------------------------
## Conclusion - For April 2019 Yellow and Green Taxi Data...

* The Green taxi service has fewer overall trips than Yellow taxi during weekday mornings and evenings
* The Green taxi service has fewer average miles traveled than Yellow taxi during weekday morning and evenings
* The Yellow taxi service serves primarily in the Manhattan region
* Green taxis are able to branch out and pick up passengers in other NYC buroughs 
* In general, yelow and green taxi pick up zones do not overlap
* However, yellow and green taxi drop off zones do overlap