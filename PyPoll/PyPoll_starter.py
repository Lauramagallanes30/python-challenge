# -*- coding: UTF-8 -*-
"""PyPoll Homework - Election Analysis."""

# Import necessary modules
import csv
import os

# Define file paths
file_to_load = os.path.join("/Users/lauramitchellemagallanes/Downloads/python-challenge/PyPoll/Resources", "election_data.csv")  # Input file path
file_to_output = os.path.join("/Users/lauramitchellemagallanes/Downloads/python-challenge/PyPoll/analysis", "election_analysis.txt")  # Output file path

# Initialize variables
total_votes = 0
candidates = {}

# Open the CSV file and process it
with open(file_to_load, mode='r') as file:
    reader = csv.reader(file)
    header = next(reader)  # Skip the header row
    
    # Tally the votes for each candidate
    for row in reader:
        total_votes += 1
        candidate = row[2]  # Candidate name is in the 3rd column
        
        # Increment the vote count for the candidate
        if candidate in candidates:
            candidates[candidate] += 1
        else:
            candidates[candidate] = 1

# Calculate percentages and determine the winner
winner = None
max_votes = 0
output = (
    "Election Results\n"
    "-------------------------\n"
    f"Total Votes: {total_votes}\n"
    "-------------------------\n"
)

# Loop through the candidates to calculate vote percentages and find the winner
for candidate, votes in candidates.items():
    vote_percentage = (votes / total_votes) * 100
    output += f"{candidate}: {vote_percentage:.3f}% ({votes})\n"
    
    # Check if this candidate has the most votes
    if votes > max_votes:
        max_votes = votes
        winner = candidate

output += (
    "-------------------------\n"
    f"Winner: {winner}\n"
    "-------------------------\n"
)

# Print the results to the terminal
print(output)

# Write the results to the text file
with open(file_to_output, mode='w') as file:
    file.write(output)
