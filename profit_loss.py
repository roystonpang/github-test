from pathlib import Path
import re, csv

def profitloss_function(forex):
    """
    - This function will determine the day where net profit is lower
    than the previous day and its value difference (converted from USD to SGD)
    - Parameter forex is predetermined, no other parameter required
    """
    #file path for profit & loss .csv is created 
    home = Path.cwd()/'csv_reports'/'profit & loss.csv'
    
    #empty list to store to store data from profit & loss.csv
    profit_loss_list = []
    
    #context manager to open file in "read" mode 
    with home.open(mode='r',encoding='UTF-8',newline='') as file:
        reader = csv.reader(file)
    #for loop is used and all data is appeneded to the empty list as dictionary
        for line in reader:
            profit_loss_list.append({"day": line[0], "net profit": line[4]})
    #header is removed
    profit_loss_list.pop(0)

    net_profit = 0
    difference = []
    day = []
    for amount in profit_loss_list:
    #condition to check if net profit figure in csv is less than the previous day    
        if float(amount["net profit"]) < net_profit:
            #the difference is multiplied by the conversion rate and appended to difference list
            difference.append((net_profit - float(amount["net profit"])) * forex)
            #corresponding day will be appended to day list
            day.append(amount["day"])
        #previous day net profit is stored    
        net_profit = float(amount["net profit"]) 

    return day, difference
