# Python-Challenge
This challenge is divided into two parts: PyBank (part 1) and PyPoll (part 2). 

## PyBank: Create a Python script that analyzes the financial records of a company

First, I imported the dataset named budget_data.csv, the dataset contained the columns Date and Profit/Losses.

I calculated the total number of months in the dataset by setting monthcount to 0 and counting the number of rows after the header.

I calculated the net total amount of Profit/Losses over the entire period by setting total to 0 and adding the values in each row.

I calculated the changes in Profit/Losses over the entire period by storing the month and difference in Profit/Losses between two consecutive rows in a list, and calculated the average of those changes by adding all values in the list and dividing it by the number of items in the list.

I calculated the greatest increase in profits by comparing all changes in profits between consecutive rows and stored the largest value in increase.

I calculated the greatest decrease in profits by comparing all changes in profits between consecutive rows and stored the smallest value in decrease.

Then, I created a text file with Python and stored the total number of months in the dataset, the total amount of "Profits/Losses" over time, the changes in "Profits/Losses" month to month during the entire period, the average change in "Profits/Losses", the greatest increase in profits, and the greatest decrease in profits.

## PyPoll: Create a Python script that analyzes election data

First, I imported the dataset named election_data.csv, the dataset contained the columns Voter ID, County, and Candidate.

I calculated the total number of votes cast by setting votecount to 0 and counting the number of rows after the header.

I created a list that stored the names of all the candidates that received votes.

I obtained the total number of votes each candidate won by setting a counter for the votes cast for each candidate and stored the totals in a list.

I obtained the percentage of votes each candidate won by dividing the number of votes each candidate received by the total votecount and multiplied the result by 100, and stored the percentages in a list.

Then, I created a text file with Python and stored the total number of votes cast, the list of candidates who received votes, the percentage of votes each candidate received, the number of votes each candidate received, and the winner of the election.
