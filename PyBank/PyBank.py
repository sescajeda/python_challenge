#Import Modules 
import os 
import csv 

#Create path to read csv file with data 
csvpath = os.path.join( 'Resources', 'budget_data.csv')

# Read csv 
with open(csvpath) as csvfile: 
    csvreader = csv.reader(csvfile, delimiter=',')
    #identify variables 
    total_months=0
    net_total=0
    greatest_decrease = 0 
    greatest_increase = 0 
    change = 0 
    total_change = 0 
    #skip title row
    next (csvreader) 
    #this is to help with the calculating changes in profit/loss so you dont calculate a change with the first row 
    previous_value = False 
    #will loop through all rows in my csv file
    for row in csvreader:
        #counts number of months
        total_months = total_months + 1
        #add the net proft/loss 
        net_total = net_total +int(row[1])
        #calculate changes 
        current_value = int(row[1])
    
        #go through each row to find the change 
        if previous_value is not False:
            #calculate profit/loss change from previous month to current
            change = current_value - previous_value
            #add new change total change 
            total_change = total_change + change
            #check if change is new greatest increase or greatest decrease 
            if change > greatest_increase:
                greatest_increase = change 
                date_greatest_increase = row[0]
            if change < greatest_decrease: 
                greatest_decrease = change 
                date_greatest_decrease = row[0]
            else: 
                greatest_increase = greatest_increase
                greatest_decrease = greatest_decrease
        previous_value = current_value 
   
    #calculate average net proft/loss 
    average_change = round ((total_change / (total_months - 1)), 2)

    #print statements 
    print ("Financial Analysis")
    print("----------------------------------")
    print ("Total Months: " + str(total_months))
    print("Total: $" + str(net_total))
    print("Average Change: $" + str(average_change))
    print("Greatest Increase in Profits: " + str(date_greatest_increase) + " ($" + str(greatest_increase) + ")")
    print("Greatest Decrease in Profits: " + str(date_greatest_decrease) + " ($" + str(greatest_decrease) + ")")


#Name text file i want to create
file_name = "Financial_Analysis.txt"

 # Write results into a new text file 
with open(file_name, "w") as file: 
    file.write("Financial Analysis.\n")
    file.write("-------------------------\n")
    file.write("Total Months: " + str(total_months) + "\n")
    file.write("Total: $" + str(net_total) + "\n")
    file.write("Average Change: $" + str(average_change) + "\n")
    file.write("Greatest Increase in Profits: " + str(date_greatest_increase) + " ($" + str(greatest_increase) + ")" + "\n")
    file.write("Greatest Decrease in Profits: " + str(date_greatest_decrease) + " ($" + str(greatest_decrease) + ")" + "\n")