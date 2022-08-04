from pathlib import Path
import re, csv

def coh_function(forex):
  home = Path.cwd()/'csv_reports'/'cash on hand.csv'
  cash_on_hand_list = []
  with home.open(mode='r',encoding='UTF-8',newline='') as file:
        reader = csv.reader(file)
      
        for line in reader:
            cash_on_hand_list.append({"day": line[0], "cash_on_hand": line[1]})
            
    cash_on_hand_list.pop(0)
