with open('task2/task2input.txt') as taskinput:
    # taskinputread = taskinput.read()
    # listedinput = taskinputread.splitlines()
    setinput = [item.split(' ') for item in taskinput.readlines()]
    #convert the second item to an integer
    setinput = [[item[0], int(item[1])] for item in setinput]
print(setinput)

def task1compute(input):
    horizontalPosition = 0
    depthPosition = 0
    for item in input:
        if item[0] == 'forward':
            horizontalPosition += item[1]
        elif item[0] == 'down':
            depthPosition += item[1]
        elif item[0] == 'up':
            depthPosition -= item[1]
    productPosition = horizontalPosition * depthPosition
    return([horizontalPosition, depthPosition, productPosition])
task1result = task1compute(setinput)

def task2compute(input):
    horizontalPosition = 0
    depthPosition = 0
    aim = 0
    for item in input:
        if item[0] == 'forward':
            horizontalPosition += item[1]
            depthPosition += item[1] * aim
        elif item[0] == 'down':
            aim += item[1]
        elif item[0] == 'up':
            aim -= item[1]
    productPosition = horizontalPosition * depthPosition
    return([horizontalPosition, depthPosition, productPosition])
task2result = task2compute(setinput)
        
print('(Part1) The horizontal position is ' + str(task1result[0]))
print('(Part1) The depth position is ' + str(task1result[1]))
print('(Part1) The product of the horizontal position and the depth position is ' + str(task1result[2]))

print('(Part2) The horizontal position is ' + str(task2result[0]))
print('(Part2) The depth position is ' + str(task2result[1]))
print('(Part2) The product of the horizontal position and the depth position is ' + str(task2result[2]))



