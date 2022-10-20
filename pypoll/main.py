
import os
import csv

# Create variables
total_votes = 0
candidates = []
candidate_votes = {}
vote_percentage = 0
percentages = []
winner = ""
winner_vote = 0

# Open CSV
csvpath = os.path.join('.', 'Resources', 'election_data.csv')
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)  

# count ballots
    for row in csvreader: 
        total_votes = total_votes + 1
                
        if row[2] not in candidate_votes:
            candidate_votes[row[2]] = 1
        else:
            candidate_votes[row[2]] += 1 

for candidate in candidate_votes:
    vote_percentage = candidate_votes.get(candidate) / total_votes * 100
    percentages.append(vote_percentage)
    if candidate_votes.get(candidate) > winner_vote:
        winner = candidate
        winner_vote = candidate_votes.get(candidate)


# Print results
print("Election Results")
print("----------------------------")
print(f"Total Votes:  {total_votes}")
print("----------------------------")
for candidate in candidate_votes:
    print(f"{candidate}: {vote_percentage:.3f}% {candidate_votes.get(candidate)}")
print("----------------------------")
print(f"Winner: {winner}")
print("----------------------------")

# Output files
output_file = os.path.join('.', 'analysis', 'election_results.txt')
with open(output_file,"w") as file:

# Write methods to print to Financial_Analysis_Summary 
    file.write("Election Results")
    file.write("\n")
    file.write("----------------------------")
    file.write("\n")
    file.write(f"Total Votes: {total_votes}")
    file.write("\n")
    file.write("----------------------------")
    file.write("\n")
    for candidate in candidate_votes:
        file.write(f"{candidate}: {vote_percentage:.3f}% {candidate_votes.get(candidate)}")
        file.write("\n")
    file.write("----------------------------")
    file.write("\n")
    file.write(f"Winner: {winner}")
    file.write("\n")
    file.write("----------------------------")


# print(total_votes)
# print(candidates)
# print(candidate_votes)
# print(percentages)
# print(winner)
# print(winner_vote)





