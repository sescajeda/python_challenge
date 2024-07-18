#Import Modules 
import os 
import csv 

#Create path to read csv file with data 
csvpath = os.path.join( 'Resources', 'election_data.csv')

# Read csv 
with open(csvpath) as csvfile: 
    csvreader = csv.reader(csvfile, delimiter=',')
    #identify_variables
    total_votes = 0 
    candidates ={}
    #skip title row
    next (csvreader) 
    #loop through each row in my csv file 
    for rows in csvreader: 
        #add value to total votes 
        total_votes = total_votes + 1
        #check all rows and add new candidates to my list 
        if rows[2] in candidates.keys():
            candidates[rows[2]]= candidates[rows[2]] + 1
        else:
            candidates[rows[2]]=1    

    #print results 
    print ("Election Results")
    print("-------------------------------")    
    print ("Total Votes:  "+ str(total_votes))
    print("-------------------------------")   
    winner = 0
    for key in candidates:
        #calculate % of votes received for each candidate 
        percent_votes = round((int(candidates[key])/int(total_votes))*100, 3)
        #determine the winner 
        if percent_votes > 50:
            winner = key 
        print(f"{key}: {percent_votes}% ({candidates[key]})")
    print("-------------------------------")   
           
    print ("Winner:  " + winner)    
    print("-------------------------------")  

#Name folder i want my text file to be created in 
existing_folder = ('analysis')

 #Name text file i want to create
file_name = os.path.join(existing_folder, "Election_Results.txt")


 # Write results into a new text file 
with open(file_name, "w") as file: 
    file.write ("Election Results\n")
    file.write("-------------------------------\n")    
    file.write ("Total Votes:  "+ str(total_votes) + "\n")
    file.write("-------------------------------\n")   
    winner = 0
    for key in candidates:
        #calculate % of votes received by each candidate 
        percent_votes = round((int(candidates[key])/int(total_votes))*100, 3)
        #determine the winner 
        if percent_votes > 50:
            winner = key 
        file.write(f"{key}: {percent_votes}% ({candidates[key]})\n")
    file.write("-------------------------------\n")   
           
    file.write ("Winner:  " + winner + "\n")    
    file.write("-------------------------------\n")  