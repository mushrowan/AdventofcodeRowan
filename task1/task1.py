
# It is good practice to use the with keyword when 
# dealing with file objects. The advantage is that 
# the file is properly closed after its suite finishes, 
# even if an exception is raised at some point. 
# Using with is also much shorter than writing equivalent 
# try-finally blocks:

#opens file, gets split data, converts every item to integer, closes the data
with open('task1/task1input.txt') as task1input:
    read_data = task1input.read()
    split_data = read_data.splitlines()

# List comprehension - this *should* make a new list which changes every item in the split data into integers
    split_data = [int(stritem) for stritem in split_data]


def trackIncreases(inputList):
    indextracker = 1
    increasetracker = 0
    for number in inputList[1:]:
        if inputList[indextracker] > inputList[indextracker - 1]:
            increasetracker += 1
        indextracker +=1
    return(increasetracker)



# more elegant way of doing the previous task, using an enumerate object (tuple)
enumeratedsplitdata = list(enumerate(split_data))
increasetracker2 = 0
for index, item in enumeratedsplitdata[1:]:
    if item > enumeratedsplitdata[index-1][1]:
        increasetracker2 += 1
print ("increasetracker2's value is " + str(increasetracker2))

# for the sum of each possible window of 3 data points, how many times does the sum increase between two windows?
# creates a list of windowdata
windowdata = [enumeratedsplitdata[index-2][1] + enumeratedsplitdata[index-1][1] + enumeratedsplitdata[index][1] for index, item in enumeratedsplitdata[2:]]
# print(windowdata)
print(trackIncreases(windowdata))



