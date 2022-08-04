from pathlib import Path
import re, csv

def overhead_function(forex):
  home = Path.cwd()/'csv_reports'/'overheads.csv'
  expenses_list = []
  with home.open(mode='r',encoding='UTF-8',newline='') as file:
        reader = csv.reader(file)
        for line in reader:
            expenses_list.append({"category": line[0], "overheads": line[1]})
  expenses_list.pop(0)
  
  max_category = None
  max_overheads = 0
  
  for expense in expenses_list:
    if int(expense["overheads"].replace(",","")) > max_overheads:
      max_overheads = int(expense["overheads"].replace(",",""))
      max_category = expense["category"]
  
  return max_category, max_overheads * forex
