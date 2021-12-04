with open('task3/task3input.txt') as task3input:
    # Get the lines which have one number each in them, make a list of them, consisting of a list of bit integers for each number
    taskinput = [[int(bit) for bit in binaryitem] for binaryitem in task3input.read().splitlines()]

print(taskinput)

for number in taskinput:
    

