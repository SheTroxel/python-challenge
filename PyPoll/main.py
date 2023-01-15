#import modules
import os
import csv
#establish path to data file
polldata = os.path.join("C:/Users/smtro/git/gitrepos/python-challenge/PyPoll/Resources/election_data.csv")
#"C:\Users\smtro\git\gitrepos\python-challenge\PyPoll\Resources\election_data.csv"
#open and read csv file
with open(polldata) as csvfile:
    #analy
    # e polling data to determine:
    #total number of votes cast
    #A complete list of candidates who received votes
    #The percentatge of votes each candidate won
    #The total number of votes each candiate won
    #The winner of the election based on popular vote
    #column headers: BallotID, county, candidate

     # Initialize vote tallies for all candidates.
    votes = {}   
    first_record = next(csvfile)
    #print(first_record) to debug

   #Read through the data
    for x in csv.reader (csvfile, delimiter=","):
        voterID= x[0]
        country=  x[1]
        candidate= x[2]

        if candidate not in votes:
            # New candidate. Add them to the dictionary.
            votes[candidate] = 1
        else:
            # Existing candidate. Accumulate more votes.
            votes[candidate] = votes[candidate] + 1

    # End of for loop. Done tallying.
#end of with
#get total votes for all candidates. Determine winner
totalvotes = 0 
winnername = "unknown"
winningvote=0
for candidate, candidate_votes in votes.items():
    totalvotes = totalvotes + candidate_votes
    
    if candidate_votes > winningvote:
        winnername = candidate
        winningvote =candidate_votes
    #print(candidate, candidate_votes, winnername,winningvote)
    
# Now print Election Results and Overall Total
print("Election Results")
print("---------------------------------------")
print("Total Votes: {:}".format(totalvotes))  
print("---------------------------------------")

#write text to file
PyPollfile=open("pyPollfile.txt", "w")
PyPollfile.write("Election Results\n")
PyPollfile.write("--------------------------------\n")
PyPollfile.write("Total Votes: {:}\n".format(totalvotes))  
PyPollfile.write("---------------------------------------\n")

# Print vote totals for all candidates.
for candidate, candidate_votes in votes.items():
    print("{:}: {:.3f}% ({:})".format(candidate,(candidate_votes/totalvotes*100), candidate_votes))
    PyPollfile.write("{:}: {:.3f}% {:} \n".format(candidate,(candidate_votes/totalvotes*100), candidate_votes)) 
    #find the winning candidate
   
#print and write winner names
print("---------------------------------------")
print("Winner: {:}".format(winnername))
print("---------------------------------------")
PyPollfile.write("---------------------------------------\n")
PyPollfile.write("Winner: {:}\n ".format(winnername))
PyPollfile.write("---------------------------------------\n")


