import os
import csv


total_votes = 0
candidate = ""
candidate_votes = {}
candidate_percentages ={}
winner_votes = 0
winner = ""

# open csv file
with open('election_data.csv','r', newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    csvheader=next(csvreader)

    # total vote counts
    for row in csvreader:
        total_votes = total_votes + 1
        candidate = row[2]
        if candidate in candidate_votes:
            candidate_votes[candidate] = candidate_votes[candidate] + 1
        else:
            candidate_votes[candidate] = 1

# vote percentage and identify winner
for person, vote_count in candidate_votes.items():
    candidate_percentages[person] = '{0:.0%}'.format(vote_count / total_votes)
    if vote_count > winner_votes:
        winner_votes = vote_count
        winner = person

seperater = "-------------------------"
#  results
print("Election Results")
print(seperater)
print(f"Total Votes: {total_votes}")
print(seperater)
for person, vote_count in candidate_votes.items():
    print(f"{person}: {candidate_percentages[person]} ({vote_count})")
print(seperater)
print(f"Winner: {winner}")
print(seperater)

# summary to txt
filename=input("filename: ")
save_file = filename.strip(".csv") + "_results.txt"
filepath = os.path.join(".", save_file)
with open(filepath,'w') as text:
    text.write(seperater + "\n")
    text.write(f"Total Votes: {total_votes}" + "\n")
    text.write(seperater + "\n")
    for person, vote_count in candidate_votes.items():
        text.write(f"{person}: {candidate_percentages[person]} ({vote_count})" + "\n")
    text.write(seperater + "\n")
    text.write(f"Winner: {winner}" + "\n")
    text.write(seperater + "\n")


