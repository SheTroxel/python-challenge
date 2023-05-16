# Import financial data set#First import module
import os
import csv
#find out path to data file
budgetfilelocation = os.path.join("..Resources/budget_data.csv")

#Open and read CSV 
with open(budgetfilelocation) as csvfile:
    #budgetfile=csv.reader(csvfile, delimiter= ",")
    #find header row in budgetfile and define variables
    #    month = row[0]
    #    profitLoss = row[1]
    monthread=0
    totalprofitloss=0
    changeinprofitloss=0
    # define previouus month
    previousprofitloss = 0 
    changeinprofitlosstotal=0
    greatestincrease=0
    greatestdecrease=0

    #read through the data
    for x in csv.reader(csvfile, delimiter= ","):
        month = x[0]
        profitLoss= x[1]
        
        #print("month =", month, "profitloss = ", profitLoss)
        #remove first row text from data

        if month!="Date":
            monthread= monthread+1
            profitLoss = int(profitLoss)
            totalprofitloss=totalprofitloss+profitLoss
            changeinprofitloss = profitLoss - previousprofitloss
            if previousprofitloss != 0:
                changeinprofitlosstotal = changeinprofitlosstotal+changeinprofitloss
            previousprofitloss=profitLoss
     
            if changeinprofitloss>greatestincrease:
                greatestincrease=changeinprofitloss
                greatestincreasemonth=month

            if changeinprofitloss<greatestdecrease:
                greatestdecrease=changeinprofitloss
                greatestdecreasemonth=month

#print to terminal      


print("Financial Analysis")
print("------------------------------------")
print("Total Months: ",  monthread)
print("Total: $", totalprofitloss)
print("Average Change: ${:.2f}".format(changeinprofitlosstotal/(monthread-1)))
print("Greatest Increase in Profits: {:} (${:})".format(greatestincreasemonth, greatestincrease))
print("Greatest Decrease in Profits: {:} (${:})".format(greatestdecreasemonth, greatestdecrease))

#print to text file
pyBankfile = open("pyBankfile.txt","w")
pyBankfile.write("Financial Analysis\n")
pyBankfile.write("----------------------------------------\n")
pyBankfile.write("Total Months: {:} \n".format(monthread))
pyBankfile.write("Total: ${:}/n".format(totalprofitloss))
pyBankfile.write("Average Change: ${:.2f}\n".format(changeinprofitlosstotal/(monthread-1)))
pyBankfile.write("Greatest Increase in Profits: {:} (${:})\n".format(greatestincreasemonth, greatestincrease))
pyBankfile.write("Greatest Decrease in Profits: {:} (${:})\n".format(greatestdecreasemonth, greatestdecrease))

#close file
pyBankfile.close()   

 
