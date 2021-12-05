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

    print(bingofeed)
    # lines = [[int(subline) for subline in (line.split())] for line in task4input.getline(0).split(',')]

"""format:
[
    []
]


"""

print(input)
def formatinputcards(inputcards, cardheight):
    print("""STARTINGHEREJEREWREW
    STARTING HERE""")
    outputlines = []
    for numberline in inputcards:
        if numberline != '':
            outputlines.append(numberline)
    #format the output lines: replace double spaces with single spaces, removes any lines which have a space as their prefix, so that the split doesn't include them at the beginning of lines.
    outputlines = [numberline.replace('  ', ' ').removeprefix(' ') for numberline in outputlines]
    #splits by space and replaces every string element with an integer.
    outputlines = [[int(number) for number in numberline.split(' ')] for numberline in outputlines]
    #take x number of lines, put them into a list of lists in the overall list, repeat until exhausted all
    #While there is something in output lines:
    print(outputlines)
    realoutput = []
    for index in range(len(outputlines)):
        card = []
        for iteration in range(cardheight):
            if outputlines != []:
                card.append(outputlines.pop(0))
        if card != []:
            realoutput.append(card)
    realoutput = [[[[bingonumber, False] for bingonumber in  bingoitem] for bingoitem in cardset] for cardset in realoutput]

    #structure: 
    #[[[[individual number, boolean] * 5 = bingo line] * 5 = bingo card] * n number of bingo cards]


    return(realoutput)
def bingoround(cardlist, inputfeed):
    cardlistvariable = cardlist
    inputfeedvariable = inputfeed
    bingoroundnumber = inputfeedvariable.pop(0)
    
    print(bingoroundnumber)
    for card in cardlistvariable:
        for bingoline in card:
            for bingopair in bingoline:
                checknumber = bingopair[0]
                print(bingopair[0])
                print(checknumber)
                if checknumber == bingoroundnumber:
                    print('yes')
                    bingopair[1] = True
                    print(bingopair)
                print(bingopair)
    return cardlistvariable
bingoinputlistfinalized = formatinputcards(input,5) 
print(formatinputcards(input, 5))
print(bingoround(bingoinputlistfinalized, bingofeed))
# testthingy = [54, True]
# # if testthingy[0] == 54:
# #     testthingy[1] = False
# # print(testthingy)



#NEW IDEA:
#SEE HOW MANY TURNS IT TAKES FOR A CARD TO WIN - GENERATE 10 LISTS FOR EACH CARD, FOR BOTH RANKS AND COLUMNS