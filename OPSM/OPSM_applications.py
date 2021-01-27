#usr chooses what type of forscasting option they want to go with
import OPSM_equations as equ
import openpyxl
from datetime import date

today = date.today() 

#! Find a way where you don't have to retype this on each file
import matplotlib.pyplot as plt
import pandas as pd

def main_menu():
    print('\n')
    print('+--------------------------------------------------+')
    print('| 1. Moving Average                                |')
    print('| 2. Weighted Moving Average                       |')
    print('| 3. Exponential Smoothing                         |')
    print('| 4. Simple Linear Regression                      |')
    print('| 5. Correlation Coefficient                       |')
    print('| b. Basic Stats (count, mean, std, min, max, etc) |')
    print('| g. Graph Data                                    |')
    print('| q. Quit Program                                  |')
    print('+--------------------------------------------------+')


def safely_terminate_program():

    #TODO save there information into an excel sheet here
    """
    usr_ans = input("Would you like to save any forcasts to an excel sheet [Y/N]")

    if usr_ans == 'Y' or 'y':
        main_menu()
        usr_ans = input("Choose one from the list to save: ")

        workbook = openpyxl.Workbook()
        excel_sheet = workbook.active

        save_item = excel_sheet.cell(row = 1, column = 1)
        save_item.value = "example"

        today_date = today.strftime("%d-%m-%Y")

        sheet_title = "OPSM saved Answer" + today_date

        workbook.create_sheet(index=1, title=sheet_title)
        workbook.save("test_data.xlsx")

        print("The answers were saved successfully")
        
    else:
        pass
    
    """
    print('The program was terminated safely\n')
    
    quit()




class print_data(object):
    def __init__(self, data, path_of_datafile, yaxis_units, xaxis_units):
        self.data = data
        self.path_of_datafile = path_of_datafile
        self.yaxis_units = yaxis_units
        self.xaxis_units = xaxis_units

    def basic_stats(self):
        print(pd.DataFrame(self.data).describe())
    
    def graph(self): 
        print('The graph of the Data will appear on an another screen shortly\n')

        plt.plot(self.data)
        plt.title(self.path_of_datafile)
        plt.ylabel(self.yaxis_units)
        plt.xlabel(self.xaxis_units)
        plt.show()

    def moving_average(self):
        print('The Moving Average: \n')
        moving_amt = int(input("What is the moving amount: "))
        moved_avg = equ.moving_average(self.data, moving_amt)
        print(moved_avg)

    def moving_average(self, data):
        print('The Moving Average: \n')
        moving_amt = int(input("What is the moving amount: "))
        moved_avg = equ.moving_average(data, moving_amt)
        print(moved_avg)



    def weighted_moving_average(self):
        print('Weighted Moving Average: \n')
        moving_amt = int(input("What is the moving amount: "))
        weight = int(input("What is the weight: "))
        weighted_moved_avg = equ.weighted_moving_average(self.data, moving_amt, weight)
        print(weighted_moved_avg)

    def weighted_moving_average(self, data):
        print('Weighted Moving Average: \n')
        moving_amt = int(input("What is the moving amount: "))
        weight = int(input("What is the weight: "))
        weighted_moved_avg = equ.weighted_moving_average(data, moving_amt, weight)
        print(weighted_moved_avg)
        

    def exponential_smoothing_forcast(self):
        print('Exponential Smoothing: \n')

    def simple_linear_regression_forcast(self):
        print('Simple Linear Regression: \n')

    def correlation_coefficient(self):
        print('Correlation Coefficient: \n')