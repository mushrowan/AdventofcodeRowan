with open('task3/task3input.txt') as task3input:
    # Get the lines which have one number each in them, make a list of them, consisting of a list of bit integers for each number
    taskinput = [[int(bit) for bit in binaryitem] for binaryitem in task3input.read().splitlines()]

print(taskinput)

gammaoutput = []
epsilonoutput = []
for number in range(0, len(taskinput[0])):
    zerocount = 0
    onecount = 0
    for binaryset in taskinput:
        if binaryset[number] == 0:
            zerocount += 1
        elif binaryset[number] == 1:
            onecount += 1
    if zerocount > onecount:
        gammaoutput.append(0)
        epsilonoutput.append(1)
    elif onecount > zerocount:
        gammaoutput.append(1)
        epsilonoutput.append(0)
print('The gamma output is '+ str(gammaoutput))
print('The epsilon output is ' + str(epsilonoutput))
stringgamma = ''
stringepsilon = '' 
for item in gammaoutput:
    stringgamma += str(item)
for item in epsilonoutput:
    stringepsilon += str(item)
print(stringgamma)
print(stringepsilon)
gammaanswer = int(stringgamma,2)
epsilonanswer = int(stringepsilon,2)

multiplyanswer = gammaanswer * epsilonanswer
print(multiplyanswer)
# Part 2 
gammaoutput = []
epsilonoutput = []
def narrowdown(inputlist, index):
    for number in range(0, len(taskinput[0])):
        zerocount = 0
        onecount = 0
        for binaryset in taskinput:
            if binaryset[number] == 0:
                zerocount += 1
            elif binaryset[number] == 1:
                onecount += 1
        if zerocount > onecount:
            gammaoutput.append(0) 
            epsilonoutput.append(1)
        elif onecount > zerocount:
            gammaoutput.append(1)
            epsilonoutput.append(0)