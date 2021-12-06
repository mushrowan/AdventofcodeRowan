#bingo: which will win first?
#beginning of round: take number, fill in grid (probably with a list pair for each number saying whether it is filled in or not)
# split by line. if a line has every index filled, or every line has a certain index filled, consider it done.
#SPLIT BY LINE, THEN SPLIT BY SPACE, THEN TURN EVERYTHING INTO INTEGERS
#end of round: check, has anybody won?
 # DEF A FUNCTION THAT TAKES AN INPUT OF NUMBER OF LINES PER BINGO CARD
# testint = int("34 ") <---- this works! so whitespaces are automatically not considered
# print(testint)
# FIND THE FIRST INSTANCE OF A NEW LINE, 
with open('task4/task4input.txt') as task4input:
    input = task4input.read().splitlines()
    bingofeed = input.pop(0)
    bingofeed = bingofeed.split(',')
    bingofeed = [int(item) for item in bingofeed]

    print(bingofeed)
    # lines = [[int(subline) for subline in (line.split())] for line in task4input.getline(0).split(',')]



# print(input)
# def formatinputcards(inputcards, cardheight):
#     print("""STARTINGHEREJEREWREW
#     STARTING HERE""")
#     outputlines = []
#     for numberline in inputcards:
#         if numberline != '':
#             outputlines.append(numberline)
#     #format the output lines: replace double spaces with single spaces, removes any lines which have a space as their prefix, so that the split doesn't include them at the beginning of lines.
#     outputlines = [numberline.replace('  ', ' ').removeprefix(' ') for numberline in outputlines]
#     #splits by space and replaces every string element with an integer.
#     outputlines = [[int(number) for number in numberline.split(' ')] for numberline in outputlines]

print("""STARTINGHEREJEREWREW
STARTING HERE""")
outputlines = []
for numberline in input:
    if numberline != '':
        outputlines.append(numberline)
    #format the output lines: replace double spaces with single spaces, removes any lines which have a space as their prefix, so that the split doesn't include them at the beginning of lines.
outputlines = [numberline.replace('  ', ' ').removeprefix(' ') for numberline in outputlines]
    #splits by space and replaces every string element with an integer.
outputlines = [[int(number) for number in numberline.split(' ')] for numberline in outputlines]
print(outputlines)


def getblock(allbingocards):
    bingoblock = []
    #Append the first 5 (length of lines) horizontal lines to the current bingo block to be tested. remove them from the overall list of all cards. 
    for number in range(5):
        bingoblock.append(allbingocards.pop(0))
    #Generate another set of lists with the vertical lines.
    columnset = []
    for index in range(len(bingoblock)):
        indexcolumn = []
        for item in bingoblock:
            indexcolumn.append(item[index])
        print(indexcolumn)
        columnset.append(indexcolumn)
    #append the horizontal and vertical lists together.
    for subitem in columnset:
        bingoblock.append(subitem)
    return(bingoblock)


testblock = getblock(outputlines)

# convert all values to our system for checking.
testblock = [[[subitem, False] for subitem in line] for line in testblock]


print(testblock)

#This checks if any numbers in a line match a bingo input. If it does, it changes the value [1] of the number to True. It can work for multiple numbers. THIS CHANGES THE INPUT LIST.

def checknumber(inputset, inputnumber):
    for subitem in inputset:
        if subitem[0] == inputnumber:
            subitem[1] = True
    return(inputset)

# This checks to see if every [1] value in a line is true. if it is, it returns the list of numbers. if it doesn't, it returns false.
def checktrue(inputset):
    possiblewin = []
    for subitem in inputset:
        if subitem[1] == True:
            possiblewin.append(subitem[0])
            continue
        else:
            print('No match for this line.')
            possiblewin = False
            break
    return(possiblewin)

def checkwin(inputset):
    count = 0
    for item in inputset:
        if item[1] == True:
            count += 1
            if count == len(inputset):
                return (True)
        else:
            return False

# sample input list
samplelist = [[33, False], [49, False], [72, False], [55, False], [73, False]]
#find how long it takes for a specific line to win
def checklist(inputset, inputfeed):
    count = 0
    winninglist = []
    for item in range(len(inputfeed)):

        inputfeedpop = inputfeed 
        singleinputnumber = inputfeedpop.pop(0)
        print(singleinputnumber)
        inputset = checknumber(inputset, singleinputnumber)
        count += 1
        winninglist = checktrue(inputset)
        if checkwin(inputset) == True:
            break
    return(inputset, count)

topcount = 0
toplist = []
for list in testblock:
    if checklist(list,bingofeed)[1] > topcount:
        topcount == checklist(samplelist,bingofeed)[1]
        toplist == checklist(samplelist,bingofeed)[1]
    

print(checklist(samplelist,bingofeed))