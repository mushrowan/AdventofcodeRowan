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
    outputlines = []
    for numberline in inputcards:
        if numberline is not '':
            outputlines.append(numberline)
    #format the output lines: replace double spaces with single spaces, removes any lines which have a space as their prefix, so that the split doesn't include them at the beginning of lines.
    outputlines = [numberline.replace('  ', ' ').removeprefix(' ') for numberline in outputlines]
    #splits by space and replaces every string element with an integer.
    outputlines = [[int(number) for number in numberline.split(' ')] for numberline in outputlines]
    #take x number of lines, put them into a list of lists in the overall list, repeat until exhausted all
    for pass in [0:cardheight]:
        outputlines = []
    return(outputlines)
print(formatinputcards(input))
    

