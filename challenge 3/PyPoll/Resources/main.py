import csv
from pathlib import Path

# Define the file path
file_path = Path("/Users/manahilrashid/Downloads/challenge 3/PyPoll/Resources/election_data 2.csv")

# Initialize variables
total_votes = 0
candidate_votes = {}

# Open and read the CSV file
with open(file_path, 'r') as file:
    reader = csv.reader(file)
    header = next(reader)  # Skip the header row
    
    for row in reader:
        candidate = row[2]
        
        # Calculate the total number of votes
        total_votes += 1
        
        # Calculate the total number of votes each candidate won
        if candidate not in candidate_votes:
            candidate_votes[candidate] = 0
        candidate_votes[candidate] += 1

# Calculate the percentage of votes each candidate won and determine the winner
winner = None
winner_votes = 0
results = []
for candidate, votes in candidate_votes.items():
    percentage = (votes / total_votes) * 100
    results.append(f"{candidate}: {percentage:.3f}% ({votes})")
    
    if votes > winner_votes:
        winner_votes = votes
        winner = candidate

# Print the analysis to the terminal
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
for result in results:
    print(result)
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

# Export the results to a text file
output_path = Path("/Users/manahilrashid/Downloads/challenge 3/PyPoll/Resources/election_data 2.txt")
with open(output_path, 'w') as file:
    file.write("Election Results\n")
    file.write("-------------------------\n")
    file.write(f"Total Votes: {total_votes}\n")
    file.write("-------------------------\n")
    for result in results:
        file.write(result + "\n")
    file.write("-------------------------\n")
    file.write(f"Winner: {winner}\n")
    file.write("-------------------------\n")
