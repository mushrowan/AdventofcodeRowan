with open('task2/task2input.txt') as taskinput:
    taskinputread = taskinput.read()
    listedinput = taskinputread.splitlines()
    setinput = [item.split(' ') for item in listedinput]
    #convert the second item to an integer
    setinput = [[item[0], int(item[1])] for item in setinput]
print(setinput)
horizontalPosition = 0
depthPosition = 0
for item in setinput:
    if item[0] == 'forward':
        horizontalPosition += item[1]
    elif item[0] == 'down':
        depthPosition += item[1]
    elif item[0] == 'up':
        depthPosition -= item[1]
productPosition = horizontalPosition * depthPosition
    
print('The horizontal position is ' + str(horizontalPosition))
print('The depth position is ' + str(depthPosition))
print('The product of the horizontal position and the depth position is ' + str(productPosition))
