#bingo: which will win first?
#beginning of round: take number, fill in grid (probably with a list pair for each number saying whether it is filled in or not)
# split by line. if a line has every index filled, or every line has a certain index filled, consider it done.
#SPLIT BY LINE, THEN SPLIT BY SPACE, THEN TURN EVERYTHING INTO INTEGERS
#end of round: check, has anybody won?
 # DEF A FUNCTION THAT TAKES AN INPUT OF NUMBER OF LINES PER BINGO CARD
# testint = int("34 ") <---- this works! so whitespaces are automatically not considered
# print(testint)
# FIND THE FIRST INSTANCE OF A NEW LINE, 
# # with open('task4/task4toyinput.txt') as task4input:
# #     input = task4input.read().splitlines()
# #     bingofeed = input.pop(0)
# #     bingofeed = bingofeed.split(',')
# #     bingofeed = [int(item) for item in bingofeed]
# #     lines = [[int(subline) for subline in (line.split())] for line in task4input.getline(0).split(',')]
# #     print(bingofeed)
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
with open('task4/task4input.txt') as taskinput:
    allblocksunformatted = taskinput.read().splitlines()
    allblockscount = 0
    allblocks = []
    for item in allblocksunformatted: 
        allblockscount += 1
        if allblockscount % 6 != 0:
            allblocks.append(item)
    allblocks = [item.removeprefix(' ') for item in allblocks]
    allblocks = [[[int(number), False] for number in (item.split())] for item in allblocks]
    print("unsegregated rows: " + str(allblocks))
# Checks both horizontal and vertical for 5 in a row - range(5) can be changed to whatever list height - the first part won't need changing though. Takes card as an input.
def checktrue(inputCard):
    for cardHorizontaline in inputCard: 
        truecount = 0
        for numberpair in cardHorizontaline: # Numberpair should take the format [number, bool]
            if numberpair[1] == True:
                truecount +=1
            else:
                truecount = 0
        if truecount >= 5:
            return(True)
      
            
    for checktrueindex in range(5):
        truecount = 0
        for cardHorizontaline in inputCard:

            if cardHorizontaline[checktrueindex][1] == True:
                truecount += 1
                
            if truecount >= 5:
                return(True)


#marks a card against a single number, changes all corresponding numbers to True. This changes the input, and does not return anything.
def markcard(inputcard, inputnumber):
    for sublist in inputcard:
        for number in sublist:
            if number[0] == inputnumber:
                number[1] = True
#using previously defined functions, take a card and find out how many counts it takes to win.
def countcard(inputcard, inputfeed):
    count = 0
    for inputnumber in inputfeed:
        if checktrue(inputcard) == True:
            return(inputcard, count)
        markcard(inputcard, inputnumber)
        count += 1

    count = 0
    return(inputcard, count)


# Test list: the second ([1]) index of every sublist is true, so this should feedback with true.
# samplelist = [[[59, False], [98, True], [84, False], [27, False], [56, False]], [[17, False], [35, True], [18, False], [64, False], [34, False]], [[62, False], [16, True], [74, False], [26, False], [55, False]], [[21, False], [99, True], [1, False], [19, False], [93, False]], [[65, False], [68, True], [53, False], [24, False], [73, False]]]
#Test list: the second list has every item as True, so this should feedback with true.
# samplelist = [[[59, False], [98, False], [84, False], [27, False], [56, False]], [[17, True], [35, True], [18, True], [64, True], [34, True]], [[62, False], [16, False], [74, False], [26, False], [55, False]], [[21, False], [99, False], [1, False], [19, False], [93, False]], [[65, False], [68, False], [53, False], [24, False], [73, False]]]
#Test list: start from scratch with everything as false, one bingo card:
samplelist = [[[59, False], [98, False], [84, False], [27, False], [56, False]], [[17, False], [35, False], [18, False], [64, False], [34, False]], [[62, False], [16, False], [74, False], [26, False], [55, False]], [[21, False], [99, False], [1, False], [19, False], [93, False]], [[65, False], [68, False], [53, False], [24, False], [73, False]]]


#finds the lowest count list
# def countlist(inputcards, inputfeed):
#     lowestcount = 101
#     while inputcards != []:
#         allblocksslice = []
#         for number in range(5):
#             if inputcards != []:
#                 allblocksslice.append(inputcards.pop(0))
#         currentcardcount = countcard(allblocksslice, inputfeed)
#         if currentcardcount[1] < lowestcount:
#             lowestcount = currentcardcount[1]
#             currentwinner = currentcardcount[0]
#             print ("new lowest count is " + str(lowestcount))
#     return currentwinner, lowestcount

#finds the highest count list
def countlist(inputcards, inputfeed):
    lowestcount = 0
    while inputcards != []:
        allblocksslice = []
        for number in range(5):
            if inputcards[0] != []:
                allblocksslice.append(inputcards.pop(0))
        currentcardcount = countcard(allblocksslice, inputfeed)
        print(currentcardcount[1])
        if currentcardcount[1] > lowestcount:
            lowestcount = currentcardcount[1]
            currentwinner = currentcardcount[0]
            print ("new highest count is " + str(lowestcount))
    return currentwinner, lowestcount


print(countlist(allblocks, feed))
print(feed[85])
print(len(feed))
# ([[[6, False], [26, False], [69, True], [27, True], [75, False]], [[61, False], [33, True], [88, True], [38, False], [20, False]], [[9, True], [56, False], [70, False], [98, True], [82, False]], [[80, True], [76, False], [55, True], [66, True], [29, False]], [[97, True], [84, True], [42, True], [77, True], [73, True]]], 26)
#61
# card = []
# for item in allblocks:
#     card.append(item)
#     if len(card) == 5:
#         print(card)
#         card.clear()
#         print("cleared card" + str(card))
#     # print(countcard(card,feed))

    
# print(card)
# print(len(samplelist))


# ([[[63, True], [2, True], [32, True], [56, True], [52, True]], [[30, True], [11, True], [33, True], [10, True], [70, True]], [[36, True], [34, False], [88, True], [82, True], [37, True]], [[62, True], [57, True], [40, True], [28, True], [96, True]], [[58, True], [73, True], [41, True], [69, True], [85, True]]], 98)