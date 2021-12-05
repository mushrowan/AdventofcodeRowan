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

testlist = ["00100","11110","10110","10111","10101","01111","00111","11100","10000","11001","00010","01010"]
testlist = [[int(bit) for bit in binaryitem] for binaryitem in testlist]
def narrowdown(inputlist, mode):
    totallength = len(inputlist[0])
    narrowdownlist = inputlist
    for number in range(0, totallength):
        buildlist = []
        zerocount = 0
        onecount = 0
        if len(narrowdownlist) == 1:
            continue
        for binaryset in narrowdownlist:
            if binaryset[number] == 0:
                zerocount += 1
            elif binaryset[number] == 1:
                onecount += 1
        if zerocount > onecount:
            countresult = 0
        elif onecount > zerocount:
            countresult = 1
        elif onecount == zerocount:
            if mode == 'oxygen':
                countresult = 1
            elif mode == 'co2':
                countresult = 1
        print(countresult)
        for binaryset in narrowdownlist:
            if mode == 'oxygen':
                if binaryset[number] == countresult:
                    buildlist.append(binaryset)
            if mode == 'co2':
                if binaryset[number] != countresult:
                    buildlist.append(binaryset)
        narrowdownlist = buildlist
        print(narrowdownlist)
    return(narrowdownlist)
        
oxynarrow = (narrowdown(taskinput, 'oxygen'))
co2narrow = (narrowdown(taskinput, 'co2'))
print(oxynarrow)
print(co2narrow)
stringoxygen = ''
stringco2 = '' 
for item in oxynarrow[0]:
    stringoxygen += str(item)
for item in co2narrow[0]:
    stringco2 += str(item)
oxyanswer = int(stringoxygen,2)
co2answer = int(stringco2,2)
print(oxyanswer)
print(co2answer)
print(oxyanswer * co2answer)
#THIS SOLUTION IS SO BODGY BUT IT WORKS DFGHJK I AM DONE