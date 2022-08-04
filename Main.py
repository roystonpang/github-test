import api, overheads, coh, profit_loss
from pathlib import Path

def main():
    """
    - function is a combination of 4 different functions to determine real time currency conversion rate (USD to SGD),
    highest overheads, cash deficit day(s) if any and profit deficit day(s) if any
    - no parameter required
    - txt file containing the data will be created
    """
    # empty list to store all the required data
    final_list = []
    
    # append real time forex value using the api function
    forex = api.api_function()
    final_list.append(f"[REAL TIME CURRENCY CONVERSION RATE] USD1 = SGD{forex}")
    
    # assigning overheads_category and overheads_value to the 2 return values from the function
    overheads_category, overheads_value = overheads.overhead_function(forex)
    # append values to the final list
    final_list.append(f"\n[HIGHEST OVERHEADS] {overheads_category.upper()} : SGD{round(overheads_value,2)}")

    # assigning coh_day and coh_value to the 2 return values from the function
    coh_day, coh_value = coh.coh_function(forex)
    
    # condition to check how many cash deficit days
    if len(coh_day) > 0:
        # for loop is used to separate each cash deficit day and append to final list
        for number in range(len(coh_day)):
            final_list.append(f"\n[CASH DEFICIT] DAY : {coh_day[number]}, AMOUNT : SGD{round(coh_value[number],2)}")
    # condition when there are no cash deficit days and append to final list
    else:    
        final_list.append(f"\n[CASH SURPLUS] CASH ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY")

    # assigning profit_day and profit_value to the 2 return values from the function
    profit_day, profit_value = profit_loss.profitloss_function(forex)
    
    # condition to check how many profit deficit days
    if len(profit_day) > 0:
        # for loop is used to separate each profit deficit day and append to final list
        for number in range(len(profit_day)):
            final_list.append(f"\n[PROFIT DEFICIT] DAY : {profit_day[number]}, AMOUNT : SGD{round(profit_value[number],2)}")
    # condition when there are no profit deficit days and append to final list
    else:    
        final_list.append(f"\n[NET PROFIT SURPLUS] NET PROFIT ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY")

    # creation of summary report txt file
    home = Path.cwd()/'summary_report.txt'
    # write final info onto txt file
    with home.open(mode='w',encoding='UTF-8') as file:
        file.writelines(final_list)
       
main()
