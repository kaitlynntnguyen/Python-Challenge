import os
import csv

election_data = os.path.join("pypoll","resources","election_data.csv")

with open(election_data) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

  # total votes
    next(csvreader)
    votes = list(csvreader)
    total_votes = len(votes)

  # candidates
    candidates = list()
    votecount = list()
    for i in range (0,total_votes):
        candidate = votes[i][2]
        votecount.append(candidate)
        if candidate not in candidates: 
            candidates.append(candidate)
    total_candidates = len(candidates)

  # votes (and percentage of votes) /candidate
    votes = list()
    percent = list()
    for j in range (0,total_candidates):
        name = candidates[j]
        votes.append(votecount.count(name))
        percent_vote = votes[j]/total_votes
        percent.append(percent_vote)

  # winner
    winner = votes.index(max(votes))    

##### EXPECTED RESULT ######
#Election Results
#-------------------------
#Total Votes: 369711
#-------------------------
#Charles Casper Stockham: 23.049% (85213)
#Diana DeGette: 73.812% (272892)
#Raymon Anthony Doane: 3.139% (11606)
#-------------------------
#Winner: Diana DeGette
#-------------------------

# print results
    print("Election Results")
    print("----------------------------")
    print(f"Total Votes: {total_votes:,}")
    print("----------------------------")
    for p in range (0,total_candidates): 
        print(f"{candidates[p]}: {percent[p]:.3%} ({votes[p]:,})")
    print("----------------------------")
    print(f"Winner: {candidates[winner]}")
    print("----------------------------")

    # print to file
    print("Election Results", file=open("PyPoll.txt", "a"))
    print("----------------------------", file=open("PyPoll.txt", "a"))
    print(f"Total Votes: {total_votes:,}", file=open("PyPoll.txt", "a"))
    print("----------------------------", file=open("PyPoll.txt", "a"))
    for p in range (0,total_candidates): 
        print(f"{candidates[p]}: {percent[p]:.3%} ({votes[p]:,})", file=open("PyPoll.txt", "a"))
    print("----------------------------", file=open("PyPoll.txt", "a"))
    print(f"Winner: {candidates[winner]}", file=open("PyPoll.txt", "a"))
    print("----------------------------", file=open("PyPoll.txt", "a"))