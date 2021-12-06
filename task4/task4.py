#bingo: which will win first?
#beginning of round: take number, fill in grid (probably with a list pair for each number saying whether it is filled in or not)
# split by line. if a line has every index filled, or every line has a certain index filled, consider it done.
#SPLIT BY LINE, THEN SPLIT BY SPACE, THEN TURN EVERYTHING INTO INTEGERS
#end of round: check, has anybody won?
 # DEF A FUNCTION THAT TAKES AN INPUT OF NUMBER OF LINES PER BINGO CARD
# testint = int("34 ") <---- this works! so whitespaces are automatically not considered
# print(testint)
# FIND THE FIRST INSTANCE OF A NEW LINE, 
# with open('task4/task4toyinput.txt') as task4input:
#     input = task4input.read().splitlines()
#     bingofeed = input.pop(0)
#     bingofeed = bingofeed.split(',')
#     bingofeed = [int(item) for item in bingofeed]
#     lines = [[int(subline) for subline in (line.split())] for line in task4input.getline(0).split(',')]
#     print(bingofeed)
feed = [7,58,52,49,72,33,55,73,27,69,88,80,9,7,59,98,63,42,84,37,87,28,97,66,79,77,61,48,83,5,94,26,70,12,51,82,99,45,22,64,10,78,13,18,15,39,8,30,68,65,40,21,6,86,90,29,60,4,38,3,43,93,44,50,41,96,20,62,19,91,23,36,47,92,76,31,67,11,0,56,95,85,35,16,2,14,75,53,1,57,81,46,71,54,24,74,89,32,25,34]


# proposed list properties:
# [
# [[1, False], [2, False]]
# [[1, False], [3, False]]
# ]
# Check if: 
#   1. all items[1] in sublist are true
#   2. all sublist[n index][1] are true
#   
#   


with open('task4/task4toyinput.txt') as taskinput:
    allblocks = taskinput.read().splitlines()
    
    allblocks.remove('')
    allblocks = [item.removeprefix(' ') for item in allblocks]
    allblocks = [[[int(number), False] for number in (item.split())] for item in allblocks]
    #create an item which contains the first 5 elements of allblocks.
    allblocks = 

