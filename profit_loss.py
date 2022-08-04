from pathlib import Path
import re, csv

def profitloss_function(forex):
    home = Path.cwd()/'csv_reports'/'profit & loss.csv'
    profit_loss_list = []
    with home.open(mode='r',encoding='UTF-8',newline='') as file:
        reader = csv.reader(file)
        for line in reader:
            profit_loss_list.append({"day": line[0], "net profit": line[4]})
    profit_loss_list.pop(0)

    net_profit = 0
    difference = []
    day = []

    for amount in profit_loss_list:
        if float(amount["net profit"]) < net_profit:
            difference.append((net_profit - float(amount["net profit"])) * forex)
            day.append(amount["day"])
        net_profit = float(amount["net profit"]) 

    return day, difference
