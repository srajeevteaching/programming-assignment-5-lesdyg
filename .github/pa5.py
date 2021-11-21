# Programmers: Lesdy Galvez
# Course: CS151, Dr. Rajeev
# Programming Assignment:5
# Program Inputs: Ask user to input distance in miles,ask user to input location as latitude and longtitude.
# Program Outputs: Average cost for cash and average cost for credit card payments, count of all trips that\
# started or ended on a date given by user, a file of information of all trips with pickup and dropoff location that
# are within the given distance of given location.
import csv
# assign the row number to each header
TaxiID=1
TripStartDate_Time=2
TripEndDate_Time=3
Duration=4
Distance=5
Cost=6
PaymentMethod=7
Taxi_company=8
PickupLatitude=9
PickupLongtitude=10
DropoffLatitude=11
DropoffLongtitude=12

import datetime as dt

with open('taxi_data.csv','r') as file:
    for line in file:
        try:
            time = line.split(',')[0] #splits the line at the comma and takes the first bit
            time = dt.datetime.strptime(time, '%d/%m/%Y %H:%M')
            print(time)
        except:
            pass

def load_csv_taxi_file(filename):
    taxi_data = []
    try:
        file = open(filename, "r")
        line_count= 1
        for line in file:
            try:
                line_count+= 1

                line_data = line.split(",")

                line_data[TaxiID] = (line_data[TaxiID])
                line_data[TripStartDate_Time] = int(line_data[TripStartDate_Time])
                line_data[TripEndDate_Time] = int(line_data[TripEndDate_Time])
                line_data[Cost] = float(line_data[Cost])
                line_data[PaymentMethod] = line_data[PaymentMethod].strip()
                line_data[Taxi_company] = int(line_data[Taxi_company])
                line_data[PickupLatitude] = float(line_data[PickupLatitude])
                line_data[PickupLongtitude] = float(line_data[PickupLongtitude])
                line_data[DropoffLatitude] = float(line_data[DropoffLatitude])
                line_data[DropoffLongtitude] =float(line_data[DropoffLongtitude])

                taxi_data.append(line_data)
            except ValueError:
                print(line_data)
        file.close()
    except FileNotFoundError:
        print("error:File", filename, "not found")
    return taxi_data
#get list from a list
file = open("taxi_data.csv", "r")
csv_reader = csv.reader(file)

lists_from_csv = []
for row in csv_reader:
    lists_from_csv.append(row)

print(lists_from_csv)

#create output file of average
import pandas as pd

# initialise data dictionary.
data_dict ={'PaymentOption1':['Cash'],'PaymentOption2':['Credit']}

data = pd.DataFrame(data_dict)

# Write to CSV file
data.to_csv("Payment.csv")

# Print the output.
print(data)

# calculate average
import numpy as np
import csv

file = csv.reader(open('taxi_data.csv', 'r'))
data = []
for row in file:
  data.append(row)

#incase you have a header/title in the first row of your csv file, do the next line else skip it
data.pop(0)

q1 = []

for i in range(len(data)):
  q1.append(int(data[i][7]))


print ('average of PaymentMethod is:', (np.mean(q1)))


def trip_count():
    TripStartDate_Time=0
    TripEndDate_Time=0
    TripStartDate_Time=input("enter start date:")
    print("Start date is:",TripStartDate_Time)
    TripEndDate_Time=input("enter end date")
    print("End date is:",TripEndDate_Time)
    trip_count=TripStartDate_Time+TripEndDate_Time
    print("trip count is:",trip_count)
def distance_of_locations():
    from math import radians, sin, cos, acos

    print("Input coordinates of two points:")
    slat = radians(float(input("Starting latitude: ")))
    slon = radians(float(input("Ending longitude: ")))
    elat = radians(float(input("Starting latitude: ")))
    elon = radians(float(input("Ending longitude: ")))

    dist = 3, 959 * acos(sin(slat) * sin(elat) + cos(slat) * cos(elat) * cos(slon - elon))
    print("The distance is:",dist)
    distance_of_locations=dist
    print("the distance between locations entered is:",distance_of_locations)

def main():
    from math import radians, sin, cos, acos

    print("This program will load data from the taxi_data.csv file and "
          "perform some operations on it.")
    print("Loading...")
    taxi_data= load_csv_taxi_file("taxi_data.csv")
    print("Done:", len(taxi_data), "lines loaded.")
    print()
    #average
    print('average of PaymentMethod is:', (np.mean(q1)))

    #calculate distance between 2 points

    from math import radians, sin, cos, acos

    print("Input coordinates of two points:")
    slat = radians(float(input("Starting latitude: ")))
    slon = radians(float(input("Ending longitude: ")))
    elat = radians(float(input("Starting latitude: ")))
    elon = radians(float(input("Ending longitude: ")))

    distance= 3, 959 * acos(sin(slat) * sin(elat) + cos(slat) * cos(elat) * cos(slon - elon))
    print("The distance is:", distance)
    distance_of_locations = distance
    print("the distance between locations entered is:", distance_of_locations)

    #distance into miles from kilometers
    kilometre_1 = float(input("Please enter the distance of points in Kilometre as a unit: "))
    conversion_ratio_1 = 0.621371
    miles_1 = kilometre_1 * conversion_ratio_1
    print("The distance of location in Miles: ", miles_1)

    #trip count
    trip_count = TripStartDate_Time + TripEndDate_Time
    print("trip count is:", trip_count)

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
main()
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------















