#ideas:
""" 
1. format the items in a way such that we have a list of lines: [[x1,y1][x2,y2]] and a list of these. we can use a range[x:y+1] (+1 so we incluse y itself) to create lists of points. then we can create a list of intersections, and figure it out from there.




"""
# Second line should intersect with third
# Open file
with open("task5/task5toyinput.txt") as file:
    taskinput = file.read().splitlines()
    taskinput = [item.split(" -> ") for item in taskinput]
    taskinput = [[[int(coords) for coords in coords.split(",")] for coords in item] for item in taskinput]

print(taskinput)
# Open toy file
