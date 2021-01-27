#! create functions to do all the equations here
import numpy as np

def moving_average(data, moving_amt):
    moving_averages = []

    #determine the start and end of the range of indexes based on the moving amount
    start = 0
    end = start + moving_amt

    #deteremine the number of moves required to completely cover the entire array once
    number_of_moves = len(data) + 1
    number_of_moves = number_of_moves - moving_amt

    #loop the entire the array
    for i in range(number_of_moves):

        #resets the moving list every iternation, therefore, it does not add the previous amount from the last iternation
        moving_list = 0      

        for j in range(start + i, end + i):
            moving_list = moving_list + data[j]
            
        moving_list = moving_list / moving_amt
        moving_averages.append(moving_list)
        
    return moving_averages
    
#! This NOT the formula for weighted moving average and should be updated
def weighted_moving_average(data, moving_amt, weight):
    moving_list = moving_average(data, moving_amt)
    return weight * moving_list

#TODO finish this later
def exponential_smoothing_forcast():
    print("There answer here")

def simple_linear_regression_forcast():
    print("There answer here")

def correlation_coefficient():
    print("There answer here")