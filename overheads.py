from pathlib import Path
import re, csv

def overhead_function(forex):
    """
    - function will determine the highest overhead category and its value (converted from USD to SGD)
    - parameter forex is predetermined, no other parameter required
    """
    # file path for overheads.csv is created
    # the data in overheads.csv is actual usd figures and not in percentages
    home = Path.cwd()/'csv_reports'/'overheads.csv'
    
    # empty list to store data extracted from overheads.csv
    expenses_list = []

    # context manager to open file in "read" mode
    with home.open(mode='r',encoding='UTF-8',newline='') as file:
        reader = csv.reader(file)
        # for loop is used and all data is appeneded to the empty list as dictionary
        for line in reader:
            expenses_list.append({"category": line[0], "overheads": line[1]})
    # header is removed
    expenses_list.pop(0)
