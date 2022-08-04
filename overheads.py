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
    
    max_category = None
    max_overheads = 0

    for expense in expenses_list:
        # condition to check if overheads figure in csv is greater than the stored figure
        if int(expense["overheads"].replace(",","")) > max_overheads:
            # largest overheads value will be stored in max_overheads
            max_overheads = int(expense["overheads"].replace(",",""))
            # corresponding category will be stored in max_category
            max_category = expense["category"]
    
    # max_overheads value (usd) will be converted to sgd using real time forex rate
    return max_category, max_overheads * forex
