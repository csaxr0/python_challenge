# import
import os
import csv

from numpy import average

# create variables
total_months = 0
total_revenue = 0
change_list = []
highest_revenue_increase = 0
highest_revenue_decrease = 999999999999999999
highest_revenue_increase_month =""
highest_revenue_decrease_month =""
previous_net = 0

# open csv
csvpath = os.path.join('.', 'resources', 'budget_data.csv')
outfile = os.path.join('.', 'analysis', 'financial_analysis.txt')

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)

    first_row = next(csvreader)
    total_months = total_months +1
    #need total net and previous net
    total_revenue = total_revenue + int(first_row [1])
    previous_net = int(first_row [1])


    for row in csvreader:
        total_months = total_months +1
        total_revenue = total_revenue + int(row [1])

        
        # if statement to check for greatest increase
        net_change = int(row [1]) - previous_net
        previous_net = int(row [1])
        change_list.append(net_change)
        if net_change > highest_revenue_increase:
            highest_revenue_increase = net_change
            highest_revenue_increase_month = row[0]

        if net_change < highest_revenue_decrease:
            highest_revenue_decrease = net_change
            highest_revenue_decrease_month = row[0] 

average_change = sum(change_list) / len(change_list) 

output =(
    f"Financial Anyalis\n"
    f"-----------------\n"
    f"Total Months: {total_months}\n"
    f"Total: $ {total_revenue}\n"
    f"Average Change:  ${average_change:.2f}\n"
    f"Greatest Increase in profits:  {highest_revenue_increase_month} ${highest_revenue_increase}\n"
    f"Greatest decrease in profits:  {highest_revenue_decrease_month} ${highest_revenue_decrease}\n"
)
print(output)

with open(outfile,"w") as out_file:
    out_file.write(output)
    







# # calculate total months, total revenue and average change
#     for row in csvreader:
#         total_months.append(row[0])
#         total_revenue.append(int(row[1]))

#     for row in range(len(total_revenue)-1):
#         average_change.append(total_revenue[row+1]-total_revenue[row])
       

# # calulate the hightest & lowest revenue and monthl
#         highest_revenue_increase = max(average_change)
#         highest_revenue_decrease = min(average_change)
#         if highest_revenue_increase == row[1]:
#             highest_revenue_month = row[0]
            

        #highest_revenue_month = max(average_change) 
        #highest_revenue_month = min(average_change)  
        #   if name_to_check == row[0]:
        #       print_percentages(row)
   



# print(highest_revenue_month)
# print(highest_revenue_increase) 
# print(highest_revenue_decrease)
