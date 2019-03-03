#import modules
import os
import csv

#variales for calculation
count_month = 0
total_revenue = 0
current_month_revenue = 0
last_month_revenue = 0
revenue_change = 0
revenue_difference = []
months = []

# open csv file

with open('budget_data.csv','r', newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    next(csvreader)

    # total month count and avearge change in revenue
    for row in csvreader:
        count_month =count_month  + 1
        months.append(row[0])
        current_month_revenue = int(row[1])
        total_revenue = total_revenue + current_month_revenue
        if count_month > 1:
            revenue_change = current_month_revenue - last_month_revenue
            revenue_difference.append(revenue_change)
        last_month_revenue = current_month_revenue

# formula to analyze result
sum_rev_changes = sum(revenue_difference)
average_change = sum_rev_changes / (count_month - 1)
max_change = max(revenue_difference)
min_change = min(revenue_difference)
max_month_index = revenue_difference.index(max_change)
min_month_index = revenue_difference.index(min_change)
max_month = months[max_month_index]
min_month = months[min_month_index]

# print summary to user
print("Financial Analysis")
print("----------------------------------------")
print(f"Total Months: {count_month}")
print(f"Total Revenue: ${total_revenue}")
print(f"Average Revenue Change: ${average_change}")
print(f"Greatest Increase in Revenue: {max_month} (${max_change})")
print(f"Greatest Decrease in Revenue: {min_month} (${min_change})")
filename=input("summaryfile: ")
save_file = filename.strip(".csv") + "_results.txt"
filepath = os.path.join(".", save_file)
with open(filepath,'w') as text:
    text.write("Financial Analysis" + "\n")
    text.write("----------------------------------------" + "\n")
    text.write(f"Total Months: {count_month}" + "\n")
    text.write(f"Total Revenue: ${total_revenue}" + "\n")
    text.write(f"Average Revenue Change: ${average_change}" + "\n")
    text.write(f"Greatest Increase in Revenue: {max_month} (${max_change})" + "\n")
    text.write(f"Greatest Decrease in Revenue: {min_month} (${min_change})" + "\n")