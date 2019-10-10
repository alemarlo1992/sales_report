"""Generate sales report showing total melons each salesperson sold."""

def sales_report(file):

    salespeople = []
    melons_sold = []
    #Line 4 and 5 create an empty list for the sales people and number of melons sold 
    f = open(file)
    #line 7: Opens the file that we wabr to input 
    for line in f:
        #the for loop iterates through each line of the text 
        line = line.rstrip()
        #line 11: takes away any empty spaces from the txt file 
        entries = line.split('|')
        #line 13: Creates a list and sets '|' as an argument know what to divide 
        salesperson = entries[0]
        #line 15: access the name of the sales people by using the first index in list 
        melons = int(entries[2])
    #line 17: Accesses the third element in list but makes sure it is set as an interger 

        if salesperson in salespeople:
        #if the salesperson is in the list sales people then...
            position = salespeople.index(salesperson)
            #gives you the index position of the sales person in the list salespeople
            melons_sold[position] += melons
            #this will add the melons as a value every time there is a more sales 
        else:
        #if the sales person is not in sales people then...
            salespeople.append(salesperson)
            #you add sales person to sales people list 
            melons_sold.append(melons)
            #also add the melons sold to melons_sold list 

sales_report('sales-report.txt')

def range_of_salespeople(melons_sold_by_people):

    for i in range(len(salespeople))
#looping over the list in salespeople 
            print(f'{salespeople[i]} sold {melons_sold} melons')
            #print the sales person and the melons sold 

range_of_salespeople(sales_report)

