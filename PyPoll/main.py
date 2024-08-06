import os
import csv

csvpath = os.path.join('..','Resources','election_data.csv')
print(csvpath)

with open(csvpath) as csvfile:
    csvReader = csv.reader(csvfile, delimiter = ",")
    csv_header = next(csvReader)
    print(csv_header)

    total_no_voters = 0
    candidates= {}
    winner_votes = 0
    winner = ""
    for row in csvReader:
        #The total number of votes cast
        total_no_voters = total_no_voters + 1

        #A complete list of candidates who received votes
        if candidates.get(row[2]) is None:
            candidates[row[2]] = 1
        else:
            candidates[row[2]] =  candidates[row[2]] + 1

#The percentage of votes each candidate won
percentages = {}
for candidate , votes in candidates.items():
    percentage = (votes / total_no_voters) *100
    percentages[candidate] = percentage

#The winner of the election based on popular vote
for candidate , votes in candidates.items():
    if votes > winner_votes:
        winner = candidate
        winner_votes = votes

print("Election Results")
print("---------------------------")
print(f"Total votes: {total_no_voters}")
print("---------------------------")
#The total number of votes each candidate won
for candidate, votes in candidates.items():
    print(f" {candidate }:{percentages[candidate]: }% ({votes }) ")    
print("---------------------------")
print(f"Winner: {winner}")
print("---------------------------")


# Write methods to print to Election_Results_Output
csvpath = os.path.join('..','analysis','Election_Results_Output.txt')
with open(csvpath,"w") as file:
     print(csvpath)
     file.write(f"Election Results \n")
     file.write("--------------------------- \n")
     file.write(f"Total votes: {total_no_voters} \n")
     file.write("--------------------------- \n")
    #The total number of votes each candidate won
     for candidate, votes in candidates.items():
        file.write(f" {candidate }:{percentages[candidate]: }% ({votes }) \n")    
     file.write("--------------------------- \n")
     file.write(f"Winner: {winner} \n")
     file.write("--------------------------- \n")
