"""
Write a Python function that calculates the uptime percentage of a service based on the total number of hours and the number of hours the service was down. 
The function should take 2 parameters(total hours and down hours, inputted when the function is run). 
Lastly, the function should return the uptime percentage rounded to two decimal places. """
import os
import time

def uptime_percentage(total_hours, down_hours):
    uptime = total_hours - down_hours
    up_perct = (uptime / total_hours) * 100
    up_round = round(up_perct, 2)
    
    return up_round


down_time = input("What's the down time for this service in hours? \n")
total_time = input("What's the total time for this service in hours? \n")
up_percentage = uptime_percentage(float(total_time), float(down_time))

print(f"The up time percentage for the service is {up_percentage}%")