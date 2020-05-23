#* In this challenge, you are tasked with helping a small, rural town modernize its vote counting process.
#
#* You will be give a set of poll data called [election_data.csv](PyPoll/Resources/election_data.csv). The dataset is composed of three columns: `Voter ID`, `County`, and `Candidate`. Your task is to create a Python script that analyzes the votes and calculates each of the following:
#
#  * The total number of votes cast
#
#  * A complete list of candidates who received votes
#
#  * The percentage of votes each candidate won
#
#  * The total number of votes each candidate won
#
#  * The winner of the election based on popular vote.
#
#* As an example, your analysis should look similar to the one below:
#
#  ```text
#  Election Results
#  -------------------------
#  Total Votes: 3521001
#  -------------------------
#  Khan: 63.000% (2218231)
#  Correy: 20.000% (704200)
#  Li: 14.000% (492940)
#  O'Tooley: 3.000% (105630)
#  -------------------------
#  Winner: Khan
#  -------------------------

import os

import csv

csvpath = os.path.join('Resources', 'election_data.csv')

with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    
    #print(csvreader)

    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")
    
    votenum = 0
    khanvote = 0
    correyvote = 0
    livote = 0
    otooleyvote = 0
    
    for row in csvreader:
        if csvreader.line_num == 1:
            continue
        votenum = votenum + 1
        
        if row[2] == 'Khan':
            khanvote = khanvote + 1
        #print(row)
        if row[2] == 'Correy':
            correyvote = correyvote + 1
        if row[2] == 'Li':
            livote = livote + 1
       
otooleyvote = votenum - khanvote - correyvote - livote
winner = ""
if khanvote > correyvote and khanvote > livote and khanvote > otooleyvote:
    winner = "Khan"
if correyvote > khanvote and correyvote > livote and correyvote > otooleyvote:
    winner = "Correy"
if livote > khanvote and livote > correyvote and livote > otooleyvote:
    winner = "Li"
if otooleyvote > khanvote and otooleyvote > livote and otooleyvote > correyvote:
    winner = "O'Tooley"

print("Election Results")
print("-------------------------")
print("Total Votes: " + str(votenum))
print("-------------------------")
print("Khan: " + str((khanvote/votenum)*100) + "% " + str(khanvote))
print("Correy: " + str((correyvote/votenum)*100) + "% " + str(correyvote))
print("Li: " + str((livote/votenum)*100) + "% " + str(livote))
print("O'Tooley: " + str((otooleyvote/votenum)*100) + "% " + str(otooleyvote))
print("-------------------------")
print("The winner is: " + winner)
print("-------------------------")

os.chdir("analysis")

f=open("analysis.txt", "w+")

f.write("Election Results\n")
f.write("-------------------------\n")
f.write("Total Votes: " + str(votenum) + "\n")
f.write("-------------------------\n")
f.write("Khan: " + str((khanvote/votenum)*100) + "% " + str(khanvote) + "\n")
f.write("Correy: " + str((correyvote/votenum)*100) + "% " + str(correyvote) + "\n")
f.write("Li: " + str((livote/votenum)*100) + "% " + str(livote) + "\n")
f.write("O'Tooley: " + str((otooleyvote/votenum)*100) + "% " + str(otooleyvote) + "\n")
f.write("-------------------------\n")
f.write("The winner is: " + winner + "\n")
f.write("-------------------------\n")


f.close()
#Election Results
#  -------------------------
#  Total Votes: 3521001
#  -------------------------
#  Khan: 63.000% (2218231)
#  Correy: 20.000% (704200)
#  Li: 14.000% (492940)
#  O'Tooley: 3.000% (105630)
#  -------------------------
#  Winner: Khan
#  -------------------------
