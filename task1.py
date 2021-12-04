
# It is good practice to use the with keyword when 
# dealing with file objects. The advantage is that 
# the file is properly closed after its suite finishes, 
# even if an exception is raised at some point. 
# Using with is also much shorter than writing equivalent 
# try-finally blocks:

with open('task1input.txt') as task1input:
    read_data = task1input.read()
    split_data = read_data.splitlines()

# List comprehension - this *should* make a new list which changes every item in the split data into integers
    split_data = [int(stritem) for stritem in split_data]
print(split_data)



indextracker = 1
increasetracker = 0
for number in split_data[1:]:
    if split_data[indextracker] > split_data[indextracker - 1]:
        increasetracker += 1
    indextracker +=1

print(increasetracker)


# enumeratedsplitdata = list(enumerate(split_data))
# indextracker2 = 0
# for index, item in enumeratedsplitdata[1:]:
#     if item > enumeratedsplitdata[index-1]:

