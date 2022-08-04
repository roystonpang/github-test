from pathlib import Path
import re, csv

def coh_function(forex):
  """
    - function will determine the day where Cash-on-Hand is lower
    than the previous day and its value difference (converted from USD to SGD)
    - parameter forex is predetermined, no other parameter required
    """
  # file path for cash on hand.csv is created
  home = Path.cwd()/'csv_reports'/'cash on hand.csv'
  
  # empty list to store data extracted from cash on hand.csv
  cash_on_hand_list = []
  
  # context manager to open file in "read" mode
  with home.open(mode='r',encoding='UTF-8',newline='') as file:
        reader = csv.reader(file)
      
        # for loop is used and all data is appeneded to the empty list as dictionary
        for line in reader:
            cash_on_hand_list.append({"day": line[0], "cash_on_hand": line[1]})
    # header is removed        
    cash_on_hand_list.pop(0)

    cash_on_hand = 0
    difference = []
    day = []
    
    for amount in cash_on_hand_list:
      # condition to check if cash on hand figure in csv is less than the previous day
      if float(amount["cash_on_hand"]) < cash_on_hand:
        # the difference is multiplied by the conversion rate and appended to difference list
        difference.append((cash_on_hand - float(amount["cash_on_hand"])) * forex)
        # corresponding day will be appended to day list
        day.append(amount["day"])
      # previous day cash on hand is stored
      cash_on_hand = float(amount["cash_on_hand"])
      
return day, difference
