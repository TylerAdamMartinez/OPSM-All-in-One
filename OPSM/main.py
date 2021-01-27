import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import OPSM_applications as app


#TODO REMEMBER fill out this before running the test
path_of_datafile = "~/OPSM/test_data.xlsx" #entire path for the file
xaxis_units = "TIME" #dependent varible
yaxis_units = "METERS" #independent varible

#Extracting Data from the excel file and breaking it down into usable parts
data = pd.read_excel(path_of_datafile)
xdata = pd.DataFrame(data, columns = [xaxis_units])
ydata = pd.DataFrame(data, columns = [yaxis_units])

xdata_arr = []
ydata_arr = []


for i in range(xdata.size):
    xdata_arr.append(float(xdata.values[i]))

for i in range(ydata.size):
    ydata_arr.append(float(ydata.values[i]))


#run the application
print("OPSM ALL-IN-ONE Program")

Print_Data = app.print_data(data, path_of_datafile, yaxis_units, xaxis_units)

usr_ans = 'not_q'
while(usr_ans is not 'q'):

    app.main_menu()

    usr_ans = input("Select an option from the list above: ")

    if usr_ans == '1':
        Print_Data.moving_average(xdata_arr)
        Print_Data.moving_average(ydata_arr)

    elif usr_ans == '2':
        Print_Data.weighted_moving_average(xdata_arr)
        Print_Data.weighted_moving_average(ydata_arr)

    elif usr_ans == '3':
        Print_Data.exponential_smoothing_forcast()

    elif usr_ans == '4':
        Print_Data.simple_linear_regression_forcast()

    elif usr_ans == '5':
        Print_Data.correlation_coefficient()

    elif usr_ans == 'b':
        Print_Data.basic_stats()

    elif usr_ans == 'g':
        Print_Data.graph()

    elif usr_ans == 'q':
        #TODO ydata_arr is temperary and is only to be used for testing in the future usrs will be able to pick what they want to be saved and that would be saved.
        app.safely_terminate_program(ydata_arr)

    else:
        pass
